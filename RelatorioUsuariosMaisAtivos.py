

class UsuariosMaisAtivos:
    def __init__(self, emprestimos):
        self.emprestimos = emprestimos

    def listarUsuarios(self):
        return len(self.emprestimos)

    def listarUsuariosMaisAtivos(self):
        usuariosmaisativos = dict(sorted(self.emprestimos.items(), key=lambda x: x[1], reverse=True)[:8])
        return usuariosmaisativos


