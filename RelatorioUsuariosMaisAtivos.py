
class UsuariosMaisAtivos:
    def __init__(self, emprestimos):
        self.emprestimos = emprestimos

    def listarUsuarios(self):
        return len(self.emprestimos)

    def listarUsuariosMaisAtivos(self, limite):
        usuarios_ordenados = sorted(
            self.emprestimos.items(),
            key=lambda item: item[1],
            reverse=True
        )

        usuarios_mais_ativos = dict(usuarios_ordenados[:limite])
        return usuarios_mais_ativos


