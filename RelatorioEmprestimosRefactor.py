class RelatorioEmprestimos:

    def __init__(self):

        self._emprestimos = {}

    def adicionar_emprestimo(self, titulo):

        self._emprestimos[titulo] = self._emprestimos.get(titulo, 0) + 1

    def total_emprestimos(self, titulo):

        return self._emprestimos.get(titulo, 0)

    def gerar_relatorio(self):
       
        if not self._emprestimos:
            return []

        # Ordena por: -quantidade (desc), título (asc)
        relatorio_ordenado = sorted(
            self._emprestimos.items(),
            key=lambda item: (-item[1], item[0])
        )

        return relatorio_ordenado
