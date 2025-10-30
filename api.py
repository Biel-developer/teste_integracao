from flask import Flask, request, jsonify
from flask_cors import CORS
from RelatorioEmprestimos import RelatorioEmprestimos
from RelatorioUsuariosMaisAtivos import UsuariosMaisAtivos
from GeradorRelatorioMensal import GeradorRelatorioMensal

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['POST'])
def gerar_relatorio():
    dados = request.json 
    emprestimos = RelatorioEmprestimos()

    for titulo in dados.get('titulos', []):
        emprestimos.adicionar_emprestimo(titulo)

    resultado = emprestimos.gerar_relatorio()
    return jsonify(resultado)


@app.route('/api/usuarios', methods=['POST'])
def usuarios_ativos():
    dados = request.json
    usuarios = UsuariosMaisAtivos(dados['emprestimos'])
    limite = dados.get('limite', len(dados['emprestimos']))
    resultado = usuarios.listarUsuariosMaisAtivos(limite)
    return jsonify(resultado)


@app.route('/api/livros', methods=['GET'])
def relatorio_livros():
    livros = [
        {"titulo": "Dom Casmurro", "emprestimos": 45},
        {"titulo": "O Cortiço", "emprestimos": 38},
        {"titulo": "1984", "emprestimos": 35},
        {"titulo": "A Revolução dos Bichos", "emprestimos": 32},
        {"titulo": "Memórias Póstumas", "emprestimos": 28},
        {"titulo": "Grande Sertão: Veredas", "emprestimos": 25}
    ]
    return jsonify(livros)


@app.route('/api/usuarios', methods=['GET'])
def relatorio_usuarios():
    usuarios = [
        {"nome": "Maria Silva", "emprestimos": 23, "categoria": "Ouro"},
        {"nome": "João Santos", "emprestimos": 19, "categoria": "Ouro"},
        {"nome": "Ana Costa", "emprestimos": 17, "categoria": "Prata"},
        {"nome": "Pedro Oliveira", "emprestimos": 15, "categoria": "Prata"},
        {"nome": "Carla Souza", "emprestimos": 13, "categoria": "Bronze"},
        {"nome": "Lucas Ferreira", "emprestimos": 12, "categoria": "Bronze"},
    ]
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
