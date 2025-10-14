import React from 'react'
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'
// Actually, let's just use standard Tailwind div classes for speed as we didn't install shadcn components via CLI.

interface StockData {
    ticker: string
    currentPrice: number
    currency: string
    data: { date: string; price: number }[]
}

interface ComponentData {
    type: string
    data: any
}

export const GenerativeUI: React.FC<{ component: ComponentData }> = ({ component }) => {
    if (!component) return null

    if (component.type === 'stock-chart') {
        const stockData = component.data as StockData
        return (
            <div className="w-full h-[400px] border rounded-xl p-4 my-4 bg-white/5 backdrop-blur-sm border-white/10 shadow-xl">
                <div className="flex justify-between items-center mb-4">
                    <h3 className="text-xl font-bold text-gray-100">{stockData.ticker} Performance</h3>
                    <span className="text-2xl font-mono text-green-400">
                        {stockData.currency} {stockData.currentPrice}
                    </span>
                </div>
                <ResponsiveContainer width="100%" height="90%">
                    <AreaChart data={stockData.data}>
                        <defs>
                            <linearGradient id="colorPrice" x1="0" y1="0" x2="0" y2="1">
                                <stop offset="5%" stopColor="#10b981" stopOpacity={0.8} />
                                <stop offset="95%" stopColor="#10b981" stopOpacity={0} />
                            </linearGradient>
                        </defs>
                        <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                        <XAxis dataKey="date" stroke="#9ca3af" tick={{ fontSize: 12 }} />
                        <YAxis stroke="#9ca3af" domain={['auto', 'auto']} tick={{ fontSize: 12 }} />
                        <Tooltip
                            contentStyle={{ backgroundColor: '#1f2937', border: 'none', borderRadius: '8px', color: '#fff' }}
                        />
                        <Area type="monotone" dataKey="price" stroke="#10b981" fillOpacity={1} fill="url(#colorPrice)" />
                    </AreaChart>
                </ResponsiveContainer>
            </div>
        )
    }

    if (component.type === 'error') {
        return (
            <div className="p-4 bg-red-500/10 border border-red-500/50 rounded-lg text-red-200">
                Error: {JSON.stringify(component.data)}
            </div>
        )
    }

    return (
        <div className="p-4 bg-gray-800 rounded-lg text-gray-400 text-sm font-mono">
            Unknown Component Type: {component.type}
            <pre className="mt-2 text-xs opacity-50">{JSON.stringify(component.data, null, 2)}</pre>
        </div>
    )
}
