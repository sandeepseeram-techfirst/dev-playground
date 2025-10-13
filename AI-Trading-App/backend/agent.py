import yfinance as yf
import openai
import os
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StockAgent:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if self.api_key:
            openai.api_key = self.api_key
        else:
            logger.warning("OPENAI_API_KEY not found. Agent will return mock responses.")

    async def process_message(self, message: str):
        """
        Process the user message and return a structured response.
        The response follows a 'Generative UI' schema:
        {
            "text": "Here is the analysis...",
            "component": {
                "type": "stock-chart" | "financial-table" | "error",
                "data": { ... }
            }
        }
        """
        # 1. Identify Intent
        # If API key is present, use LLM. Otherwise, use simple fallback for Demo.
        try:
            extraction = await self._extract_intent(message)
            ticker = extraction.get("ticker")
            
            if not ticker:
                if not self.api_key:
                     return {
                        "text": "I see you haven't configured an OpenAI API key yet. To see a demo, try asking for 'AAPL' or 'Tesla'.",
                        "component": None
                    }
                else:
                    return {
                        "text": extraction.get("response", "I couldn't identify a stock ticker in your message. Please mention a stock symbol like AAPL or TSLA."),
                        "component": None
                    }

            # 2. Fetch Data
            try:
                stock = yf.Ticker(ticker)
                hist = stock.history(period="1mo")
                
                if hist.empty:
                     return {
                        "text": f"I couldn't find data for {ticker}. Is the symbol correct?",
                        "component": None
                    }

                # Format data for Chart
                chart_data = []
                for date, row in hist.iterrows():
                    chart_data.append({
                        "date": date.strftime("%Y-%m-%d"),
                        "price": row["Close"]
                    })
                
                info = stock.info
                summary = info.get('longBusinessSummary', 'No summary available.')
                
                return {
                    "text": f"Here is the performance of {info.get('shortName', ticker)} ({ticker}) over the last month.\n\n**Summary**: {summary[:200]}...",
                    "component": {
                        "type": "stock-chart",
                        "data": {
                            "ticker": ticker,
                            "data": chart_data,
                            "currentPrice": info.get('currentPrice', 'N/A'),
                            "currency": info.get('currency', 'USD')
                        }
                    }
                }

            except Exception as e:
                logger.error(f"Data fetch error: {e}")
                return {
                    "text": f"I encountered an error fetching data for {ticker}: {str(e)}",
                    "component": None
                }

        except Exception as e:
            logger.error(f"Processing error: {e}")
            return {
                "text": "I'm having trouble connecting to my brain. Please check your system logs.",
                "component": None
            }

    async def _extract_intent(self, message: str):
        """
        Extracts ticker using OpenAI or regex fallback.
        """
        # Fallback if no API Key (Demo Mode)
        if not self.api_key:
            message_lower = message.lower()
            if "tesla" in message_lower or "tsla" in message_lower:
                return {"ticker": "TSLA"}
            if "apple" in message_lower or "aapl" in message_lower:
                return {"ticker": "AAPL"}
            if "microsoft" in message_lower or "msft" in message_lower:
                return {"ticker": "MSFT"}
            if "nvidia" in message_lower or "nvda" in message_lower:
                return {"ticker": "NVDA"}
            return {"ticker": None}

        # LLM Extraction
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a financial assistant. Extract the stock ticker from the user's message. Return JSON: {\"ticker\": \"SYMBOL\", \"response\": \"Optional conversational response\"}. If no ticker, set ticker to null."},
                    {"role": "user", "content": message}
                ],
                response_format={"type": "json_object"}
            )
            content = response.choices[0].message.content
            return json.loads(content)
        except Exception as e:
             logger.error(f"OpenAI error: {e}")
             return {"ticker": None}
