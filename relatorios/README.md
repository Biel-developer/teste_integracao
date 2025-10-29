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
