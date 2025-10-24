class GeradorRelatorioMensal:
    def __init__(self, dados):
        self.dados_mensais = dados
        self.meses_ordenados = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"]
    def gerar_relatorio_texto(self):
        linhas_relatorio = []
        linhas_relatorio.append("--- Relatório Mensal: Empréstimos e Devoluções ---")
        for mes in self.meses_ordenados:
            if mes in self.dados_mensais:
                dados = self.dados_mensais[mes]
                linhas_relatorio.append(f"\n{mes}:")
                linhas_relatorio.append(f"  Devoluções: {dados['devoluções']}")
                linhas_relatorio.append(f"  Empréstimos: {dados['emprestimos']}")
        linhas_relatorio.append("\nRelatório gerado.")
        return "\n".join(linhas_relatorio)
