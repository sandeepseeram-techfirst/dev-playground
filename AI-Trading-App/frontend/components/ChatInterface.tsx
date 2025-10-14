"use client"

import React, { useState, useRef, useEffect } from 'react'
import { Send, Bot, User, Loader2 } from 'lucide-react'
import { GenerativeUI } from './GenerativeUI'
import { cn } from '@/lib/utils'

interface Message {
    role: 'user' | 'assistant'
    content: string
    component?: any
}

export default function ChatInterface() {
    const [messages, setMessages] = useState<Message[]>([
        { role: 'assistant', content: 'Hello! I am your AI Financial Analyst. Ask me about any stock (e.g., "Analyze AAPL").' }
    ])
    const [input, setInput] = useState('')
    const [loading, setLoading] = useState(false)
    const endRef = useRef<HTMLDivElement>(null)

    const scrollToBottom = () => endRef.current?.scrollIntoView({ behavior: 'smooth' })
    useEffect(scrollToBottom, [messages])

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        if (!input.trim() || loading) return

        const userMsg: Message = { role: 'user', content: input }
        setMessages(prev => [...prev, userMsg])
        setInput('')
        setLoading(true)

        try {
            const res = await fetch('http://localhost:8000/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userMsg.content })
            })

            if (!res.ok) throw new Error('Network response was not ok')

            const data = await res.json()
            setMessages(prev => [...prev, {
                role: 'assistant',
                content: data.text,
                component: data.component
            }])
        } catch (error) {
            setMessages(prev => [...prev, { role: 'assistant', content: "Sorry, I encountered an error connecting to the brain." }])
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="flex flex-col h-screen max-w-5xl mx-auto p-4 md:p-6">
            <header className="flex items-center gap-3 mb-6 p-4 rounded-2xl bg-gradient-to-r from-indigo-500/10 to-purple-500/10 border border-white/5">
                <div className="p-3 bg-indigo-500 rounded-xl shadow-lg shadow-indigo-500/20">
                    <Bot className="text-white w-6 h-6" />
                </div>
                <div>
                    <h1 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-400">
                        Thesys Financial Agent
                    </h1>
                    <p className="text-sm text-gray-500">Powered by OpenAI & Generative UI</p>
                </div>
            </header>

            <div className="flex-1 overflow-y-auto mb-6 space-y-6 pr-2 custom-scrollbar">
                {messages.map((m, i) => (
                    <div key={i} className={cn("flex gap-4", m.role === 'user' ? "flex-row-reverse" : "")}>
                        <div className={cn(
                            "w-10 h-10 rounded-full flex items-center justify-center shrink-0",
                            m.role === 'assistant' ? "bg-indigo-600/20 text-indigo-400" : "bg-white/10 text-white"
                        )}>
                            {m.role === 'assistant' ? <Bot size={20} /> : <User size={20} />}
                        </div>

                        <div className={cn(
                            "flex flex-col max-w-[85%]",
                            m.role === 'user' ? "items-end" : "items-start"
                        )}>
                            <div className={cn(
                                "p-4 rounded-2xl text-sm leading-relaxed shadow-sm",
                                m.role === 'assistant'
                                    ? "bg-gray-900/50 border border-white/5 text-gray-300"
                                    : "bg-indigo-600 text-white"
                            )}>
                                <div className="whitespace-pre-wrap">{m.content}</div>
                            </div>

                            {m.component && (
                                <div className="mt-3 w-full animate-in fade-in slide-in-from-bottom-4 duration-500">
                                    <GenerativeUI component={m.component} />
                                </div>
                            )}
                        </div>
                    </div>
                ))}
                {loading && (
                    <div className="flex gap-4">
                        <div className="w-10 h-10 rounded-full bg-indigo-600/20 text-indigo-400 flex items-center justify-center">
                            <Bot size={20} />
                        </div>
                        <div className="p-4 rounded-2xl bg-gray-900/50 border border-white/5 flex items-center gap-2">
                            <Loader2 className="w-4 h-4 animate-spin text-indigo-400" />
                            <span className="text-xs text-gray-500">Analyzing market data...</span>
                        </div>
                    </div>
                )}
                <div ref={endRef} />
            </div>

            <form onSubmit={handleSubmit} className="relative group">
                <input
                    className="w-full bg-gray-900/50 border border-white/10 text-white placeholder:text-gray-600 rounded-xl px-5 py-4 pr-14 focus:outline-none focus:ring-2 focus:ring-indigo-500/50 focus:border-transparent transition-all shadow-lg hover:bg-gray-900/80"
                    placeholder="Ask about a stock (e.g., AAPL analysis)..."
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    autoFocus
                />
                <button
                    type="submit"
                    disabled={loading || !input.trim()}
                    className="absolute right-2 top-2 p-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-500 disabled:opacity-50 disabled:hover:bg-indigo-600 transition-colors shadow-lg shadow-indigo-600/20"
                >
                    <Send size={18} />
                </button>
            </form>
        </div>
    )
}
