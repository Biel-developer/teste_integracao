"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from "recharts"

const data = [
  { mes: "Jan", emprestimos: 65, devolucoes: 58 },
  { mes: "Fev", emprestimos: 72, devolucoes: 68 },
  { mes: "Mar", emprestimos: 85, devolucoes: 75 },
  { mes: "Abr", emprestimos: 78, devolucoes: 82 },
  { mes: "Mai", emprestimos: 92, devolucoes: 85 },
  { mes: "Jun", emprestimos: 88, devolucoes: 90 },
]

export function BorrowingTrends() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Tendências de Empréstimos</CardTitle>
        <CardDescription>Comparação mensal de empréstimos e devoluções</CardDescription>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={350}>
          <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" className="stroke-muted" />
            <XAxis dataKey="mes" className="text-xs" />
            <YAxis className="text-xs" />
            <Tooltip
              contentStyle={{
                backgroundColor: "hsl(var(--card))",
                border: "1px solid hsl(var(--border))",
                borderRadius: "0.5rem",
              }}
            />
            <Legend />
            <Line
              type="monotone"
              dataKey="emprestimos"
              stroke="hsl(var(--chart-1))"
              strokeWidth={2}
              name="Empréstimos"
              dot={{ fill: "hsl(var(--chart-1))" }}
            />
            <Line
              type="monotone"
              dataKey="devolucoes"
              stroke="hsl(var(--chart-2))"
              strokeWidth={2}
              name="Devoluções"
              dot={{ fill: "hsl(var(--chart-2))" }}
            />
          </LineChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  )
}
