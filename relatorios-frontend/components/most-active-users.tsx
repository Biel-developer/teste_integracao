import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import { Badge } from "@/components/ui/badge"

const users = [
  { nome: "Maria Silva", emprestimos: 28, categoria: "Ouro" },
  { nome: "João Santos", emprestimos: 24, categoria: "Ouro" },
  { nome: "Ana Costa", emprestimos: 21, categoria: "Prata" },
  { nome: "Pedro Oliveira", emprestimos: 19, categoria: "Prata" },
  { nome: "Carla Souza", emprestimos: 17, categoria: "Prata" },
  { nome: "Lucas Ferreira", emprestimos: 15, categoria: "Bronze" },
  { nome: "Julia Almeida", emprestimos: 14, categoria: "Bronze" },
  { nome: "Rafael Lima", emprestimos: 12, categoria: "Bronze" },
]

const categoryColors = {
  Ouro: "bg-yellow-500/10 text-yellow-700 dark:text-yellow-400",
  Prata: "bg-gray-500/10 text-gray-700 dark:text-gray-400",
  Bronze: "bg-orange-500/10 text-orange-700 dark:text-orange-400",
}

export function MostActiveUsers() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Usuários Mais Ativos</CardTitle>
        <CardDescription>Ranking dos leitores com mais empréstimos</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="space-y-3">
          {users.map((user, index) => {
            const initials = user.nome
              .split(" ")
              .map((n) => n[0])
              .join("")
            return (
              <div
                key={user.nome}
                className="flex items-center justify-between rounded-lg border border-border p-3 transition-colors hover:bg-muted/50"
              >
                <div className="flex items-center gap-3">
                  <div className="flex h-8 w-8 items-center justify-center rounded-full bg-primary/10 text-sm font-bold text-primary">
                    {index + 1}
                  </div>
                  <Avatar className="h-10 w-10">
                    <AvatarFallback className="bg-accent text-accent-foreground">{initials}</AvatarFallback>
                  </Avatar>
                  <div>
                    <p className="font-medium">{user.nome}</p>
                    <p className="text-sm text-muted-foreground">{user.emprestimos} empréstimos</p>
                  </div>
                </div>
                <Badge variant="secondary" className={categoryColors[user.categoria as keyof typeof categoryColors]}>
                  {user.categoria}
                </Badge>
              </div>
            )
          })}
        </div>
      </CardContent>
    </Card>
  )
}
