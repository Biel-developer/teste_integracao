"use client"

import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts"

const data = [
  { titulo: "Dom Casmurro", emprestimos: 45 },
  { titulo: "O Cortiço", emprestimos: 38 },
  { titulo: "1984", emprestimos: 35 },
  { titulo: "A Revolução dos Bichos", emprestimos: 32 },
  { titulo: "Memórias Póstumas", emprestimos: 28 },
  { titulo: "Grande Sertão: Veredas", emprestimos: 25 },
]

export function MostBorrowedBooks() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Livros Mais Emprestados</CardTitle>
        <CardDescription>Top 6 livros com maior número de empréstimos</CardDescription>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" className="stroke-muted" />
            <XAxis
              dataKey="titulo"
              angle={-45}
              textAnchor="end"
              height={100}
              className="text-xs"
              tick={{ fill: "hsl(var(--muted-foreground))" }}
            />
            <YAxis tick={{ fill: "hsl(var(--muted-foreground))" }} />
            <Tooltip
              contentStyle={{
                backgroundColor: "hsl(var(--card))",
                border: "1px solid hsl(var(--border))",
                borderRadius: "0.5rem",
              }}
            />
            <Bar dataKey="emprestimos" fill="hsl(var(--chart-1))" radius={[8, 8, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  )
}
