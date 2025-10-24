"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts"

const data = [
  { titulo: "Dom Casmurro", emprestimos: 45 },
  { titulo: "O Cortiço", emprestimos: 38 },
  { titulo: "1984", emprestimos: 35 },
  { titulo: "Memórias Póstumas", emprestimos: 32 },
  { titulo: "Grande Sertão", emprestimos: 28 },
  { titulo: "A Metamorfose", emprestimos: 25 },
  { titulo: "Cem Anos de Solidão", emprestimos: 22 },
]

export function MostBorrowedBooks() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Livros Mais Emprestados</CardTitle>
        <CardDescription>Top 7 livros com maior número de empréstimos</CardDescription>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={350}>
          <BarChart data={data} layout="vertical" margin={{ left: 100, right: 20 }}>
            <CartesianGrid strokeDasharray="3 3" className="stroke-muted" />
            <XAxis type="number" className="text-xs" />
            <YAxis dataKey="titulo" type="category" className="text-xs" width={100} />
            <Tooltip
              contentStyle={{
                backgroundColor: "hsl(var(--card))",
                border: "1px solid hsl(var(--border))",
                borderRadius: "0.5rem",
              }}
            />
            <Bar dataKey="emprestimos" fill="hsl(var(--chart-1))" radius={[0, 8, 8, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  )
}
