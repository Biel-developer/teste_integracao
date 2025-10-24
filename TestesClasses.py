import unittest
import RelatorioEmprestimos
from UsuariosMaisAtivos import UsuariosMaisAtivos

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

    def setup(self):
        self.usuarios = UsuariosMaisAtivos()

    def test_listarUsuarios(self):
        result = self.usuarios
        self.assertEquals(result, 0)



if __name__ == '__main__':
  
    unittest.main()
