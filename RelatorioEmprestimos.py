class RelatorioEmprestimos:

    def __init__(self):
        self.emprestimos = {}

    def adicionar_emprestimo(self, titulo):
        if titulo in self.emprestimos:
            self.emprestimos[titulo] += 1
        else:
            self.emprestimos[titulo] = 1

    def total_emprestimos(self, titulo):
        return self.emprestimos.get(titulo, 0)

    def gerar_relatorio(self):
        if not self.emprestimos:
            return []

        resultado = []
        for titulo, count in self.emprestimos.items():
            resultado.append((titulo, count))

        resultado.sort(key=lambda x: x[1], reverse=True)

        return resultado
