
# Sistema de Relatórios da Biblioteca - Equipe 4

Sistema desenvolvido com metodologia TDD (Test-Driven Development) para geração de relatórios de biblioteca.

##Hierarquia deo projeto

# 🧩 Frontend 
📦 projeto/

┣ 📂 tests → Testes automatizados

┣ 📂 .next → Build gerado automaticamente pelo Next.js (não editar)

┣ 📂 app → Páginas e rotas principais da aplicação

┣ 📂 components → Componentes reutilizáveis da interface (botões, cards, etc.)

┣ 📂 hooks → Hooks personalizados (lógica reutilizável do React)

┣ 📂 lib → Funções utilitárias e configurações auxiliares

┣ 📂 node_modules → Dependências instaladas (gerado automaticamente)

┣ 📂 public → Imagens, ícones e outros arquivos públicos

┣ 📂 styles → Arquivos de estilo global e configurações do Tailwind

┣ 📜 .gitignore → Arquivos e pastas ignorados pelo Git

┣ 📜 components.json → Configuração dos componentes (usado por algumas libs)

┣ 📜 jest.config.js → Configuração dos testes com Jest

┣ 📜 next-env.d.ts → Tipagens padrão do Next.js

┣ 📜 next.config.mjs → Configurações gerais do Next.js

┣ 📜 package-lock.json → Controle de versões das dependências (gerado pelo npm)

┣ 📜 package.json → Lista de dependências e scripts do projeto

┣ 📜 pnpm-lock.yaml → Controle de dependências (se estiver usando pnpm)

┣ 📜 postcss.config.mjs → Configuração do PostCSS (usado pelo Tailwind)

┣ 📜 README.md → Documento explicativo do projeto

┣ 📜 tsconfig.json → Configuração do TypeScript


## 🐍 Backend
📦 projeto/

┣ 📂 pycache → Arquivos compilados automaticamente pelo Python

┣ 📂 .idea → Configurações do ambiente (PyCharm / VSCode)

┣ 📜 api.py → Arquivo principal da API (ponto de entrada do servidor Flask)

┣ 📜 GeradorRelatorioMensal.py → Classe que gera relatórios mensais

┣ 📜 RelatorioEmprestimos.py → Classe que lida com os relatórios de empréstimos

┣ 📜 RelatorioEmprestimosRefac.py → Versão refatorada do relatório de empréstimos

┣ 📜 RelatorioUsuariosMaisAtivos.py→ Classe que gera relatório dos usuários mais ativos

┣ 📜 TestesClasses.py → Testes unitários das classes principais


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

