<<<<<<< HEAD
# Sistema de Relatórios da Biblioteca - Equipe 4

Sistema desenvolvido com metodologia TDD (Test-Driven Development) para geração de relatórios de biblioteca.

## Funcionalidades

- Relatórios de livros mais emprestados
- Ranking de usuários mais ativos
- Estatísticas gerais de empréstimos
- Gráficos de tendências
- Integração com módulos de Empréstimos, Usuários e Catálogo

## Metodologia TDD

Este projeto foi desenvolvido seguindo os princípios do TDD:

1. **Red**: Escrever testes que falham
2. **Green**: Implementar código mínimo para passar nos testes
3. **Refactor**: Melhorar o código mantendo os testes passando

## Executar Testes

\`\`\`bash
# Executar todos os testes
npm test

# Executar testes em modo watch
npm run test:watch

# Gerar relatório de cobertura
npm run test:coverage
\`\`\`

## Estrutura de Testes

- `__tests__/app/` - Testes de páginas
- `__tests__/components/` - Testes de componentes
- `__tests__/setup.ts` - Configuração global dos testes

## Cobertura de Testes

Os testes cobrem:
- Renderização de componentes
- Exibição correta de dados
- Estilos condicionais
- Estrutura de layout
- Integração entre componentes
=======
# teste_integracao

## Instruções para executar o projeto (Next.js + TypeScript)

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

### 2. Acessar a pasta do projeto

```bash
cd nome-do-repositorio
```

### 3. Instalar o Node.js 

No macOS só dar esse comando

```bash
brew install node
```

### 4. Instalar as dependências do projeto

```bash
npm install
# ou
yarn
```

### 5. Iniciar o servidor de desenvolvimento

```bash
npm run dev
# ou
yarn dev
```

### 6. Acessar o projeto no navegador

Abra o navegador e acesse:

```
http://localhost:3000
```

### 7. Comandos adicionais

| Comando         | Descrição                                   |
| --------------- | ------------------------------------------- |
| `npm run build` | Cria uma versão otimizada para produção     |
| `npm run start` | Inicia o projeto após o build               |
| `npm run lint`  | Verifica o código em busca de erros de lint |

>>>>>>> f2f2678fb36cd546c93f9201048cffc1cc206a3b
