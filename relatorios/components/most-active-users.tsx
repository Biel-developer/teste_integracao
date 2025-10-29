import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import { Badge } from "@/components/ui/badge"

const users = [
  { nome: "Maria Silva", emprestimos: 23, categoria: "Ouro" },
  { nome: "João Santos", emprestimos: 19, categoria: "Ouro" },
  { nome: "Ana Costa", emprestimos: 17, categoria: "Prata" },
  { nome: "Pedro Oliveira", emprestimos: 15, categoria: "Prata" },
  { nome: "Carla Souza", emprestimos: 13, categoria: "Bronze" },
  { nome: "Lucas Ferreira", emprestimos: 12, categoria: "Bronze" },
]

function getInitials(name: string) {
  return name
    .split(" ")
    .map((n) => n[0])
    .join("")
    .toUpperCase()
}

function getCategoryColor(categoria: string) {
  switch (categoria) {
    case "Ouro":
      return "bg-yellow-500/10 text-yellow-700 dark:text-yellow-400"
    case "Prata":
      return "bg-gray-500/10 text-gray-700 dark:text-gray-400"
    case "Bronze":
      return "bg-orange-500/10 text-orange-700 dark:text-orange-400"
    default:
      return "bg-muted text-muted-foreground"
  }
}

export function MostActiveUsers() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Usuários Mais Ativos</CardTitle>
        <CardDescription>Ranking dos leitores com mais empréstimos</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          {users.map((user, index) => (
            <div key={user.nome} className="flex items-center gap-4">
              <div className="flex h-8 w-8 items-center justify-center rounded-full bg-primary/10 text-sm font-bold text-primary">
                {index + 1}
              </div>
              <Avatar>
                <AvatarFallback className="bg-accent text-accent-foreground">{getInitials(user.nome)}</AvatarFallback>
              </Avatar>
              <div className="flex-1">
                <p className="font-medium">{user.nome}</p>
                <p className="text-sm text-muted-foreground">{user.emprestimos} empréstimos</p>
              </div>
              <Badge variant="secondary" className={getCategoryColor(user.categoria)}>
                {user.categoria}
              </Badge>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  )
}
