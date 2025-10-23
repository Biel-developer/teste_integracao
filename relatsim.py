dados_mensais = {
    "Janeiro": {"devoluções": 58, "emprestimos": 65},
    "Fevereiro": {"devoluções": 68, "emprestimos": 72},
    "Março": {"devoluções": 75, "emprestimos": 85},
    "Abril": {"devoluções": 82, "emprestimos": 78},
    "Maio": {"devoluções": 85, "emprestimos": 92},
    "Junho": {"devoluções": 90, "emprestimos": 88},
}

meses_ordenados = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"]

print("\n--- Relatório Mensal: Empréstimos e Devoluções ---")

for mes in meses_ordenados:
    if mes in dados_mensais:
        dados = dados_mensais[mes]
        print(f"\n{mes}:")
        print(f"  Devoluções: {dados['devoluções']}")
        print(f"  Empréstimos: {dados['emprestimos']}")

print("\nRelatório gerado.")
