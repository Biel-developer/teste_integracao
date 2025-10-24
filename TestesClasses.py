import unittest

class RelatorioEmprestimos:
    def __init__(self):
        pass
    def adicionar_emprestimo(self, livro):
        pass
    def total_emprestimos(self, livro):
        return 0
    def gerar_relatorio(self):
        return []

class UsuariosMaisAtivos:
    def __init__(self, emprestimos):
        self.emprestimos = {}
    def listarUsuarios(self):
        return 0
    def listarUsuariosMaisAtivos(self):
        return {}

class GeradorRelatorioMensal:
    def __init__(self, dados):
        self.dados_mensais = dados
        self.meses_ordenados = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"]
    def gerar_relatorio_texto(self):
        return ""

# --- TESTES (Referenciam as classes acima) ---

class TestRelatorioEmprestimos(unittest.TestCase):

    def setUp(self):
        self.relatorio = RelatorioEmprestimos()

    def test_contar_multiplos_emprestimos(self):
        #Testa contagem de vários empréstimos do mesmo livro
        self.relatorio.adicionar_emprestimo("Clean Code")
        self.relatorio.adicionar_emprestimo("Clean Code")
        self.relatorio.adicionar_emprestimo("Clean Code")
        self.assertEqual(self.relatorio.total_emprestimos("Clean Code"), 3)

    def test_gerar_relatorio_vazio(self):
        #Testa relatório quando não há empréstimos
        resultado = self.relatorio.gerar_relatorio()
        self.assertEqual(resultado, [])

    def test_gerar_relatorio_ordenado(self):
        #Testa se o relatório retorna livros ordenados por mais emprestados
        self.relatorio.adicionar_emprestimo("Python Fluente")
        self.relatorio.adicionar_emprestimo("Clean Code")
        self.relatorio.adicionar_emprestimo("Clean Code")
        self.relatorio.adicionar_emprestimo("Design Patterns")

        resultado = self.relatorio.gerar_relatorio()

        # Espera-se: Clean Code (2), Design Patterns (1), Python Fluente (1)
        self.assertEqual(resultado[0][0], "Clean Code")
        self.assertEqual(resultado[0][1], 2)


class TestUsuariosMaisAtivos(unittest.TestCase):

    def setUp(self):
        emprestimos = {"user1": 40, "user2": 22, "user3": 7, "user4": 67, 
                       "user5": 9, "user6": 2, "user7": 94, "user8": 2000020, "user9": 93}
        self.usuarios = UsuariosMaisAtivos(emprestimos)

    def test_listarUsuarios(self):
        result = self.usuarios.listarUsuarios()
        self.assertEqual(result, 9)

    def test_listarUsuariosMaisAtivos(self):
        result = self.usuarios.listarUsuariosMaisAtivos()
        self.assertEqual(result, {'user8': 2000020, 'user7': 94, 'user9': 93, 
                                     'user4': 67, 'user1': 40, 'user2': 22, 'user5': 9, 'user3': 7})

class TestGeradorRelatorioMensal(unittest.TestCase):
    
    def setUp(self):
        self.dados_teste = {
            "Janeiro": {"devoluções": 10, "emprestimos": 20},
            "Fevereiro": {"devoluções": 30, "emprestimos": 40},
        }
        self.gerador = GeradorRelatorioMensal(self.dados_teste)
        self.gerador.meses_ordenados = ["Janeiro", "Fevereiro"]

    def test_gerar_relatorio_texto_mensal(self):
        relatorio_esperado = (
            "--- Relatório Mensal: Empréstimos e Devoluções ---\n"
            "\nJaneiro:\n"
            "  Devoluções: 10\n"
            "  Empréstimos: 20\n"
            "\nFevereiro:\n"
            "  Devoluções: 30\n"
            "  Empréstimos: 40\n"
            "\nRelatório gerado."
        )
        
        relatorio_real = self.gerador.gerar_relatorio_texto()
        
        self.assertEqual(relatorio_real, relatorio_esperado)

if __name__ == '__main__':
    unittest.main()
