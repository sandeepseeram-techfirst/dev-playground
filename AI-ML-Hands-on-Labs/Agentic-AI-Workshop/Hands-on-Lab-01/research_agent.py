import os
from langchain_openai import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# ── 1. API Key ──────────────────────────────────────────────────────────────
os.environ["OPENAI_API_KEY"] = "sk-..."  # ← replace with your key

# ── 2. Tool: Wikipedia ─────────────────────────────────────────────────────
wiki = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=800)
)

tools = [
    Tool(
        name="Wikipedia",
        func=wiki.run,
        description="Useful for looking up factual encyclopedic knowledge about people, "
                    "technologies, companies, or events."
    )
]

# ── 3. LLM Reasoning Engine ────────────────────────────────────────────────
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# ── 4. Memory ──────────────────────────────────────────────────────────────
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# ── 5. Initialise Agent ────────────────────────────────────────────────────
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    max_iterations=6
)

# ── 6. Run multi-turn research session ────────────────────────────────────

questions = [
    "What are the top AI coding assistants available today?",
    "What makes GitHub Copilot different from the others?",
    "Which would you recommend for a Python backend engineering team?"
]

for q in questions:
    print(f"
🔵 QUESTION: {q}")
    answer = agent.run(q)
    print(f"
🟢 ANSWER:
{answer}")
    print("-" * 60)