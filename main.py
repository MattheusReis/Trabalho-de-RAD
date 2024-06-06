from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Codigo Limpo: Habilidades Praticas do Agile Software.',
        'autor': 'Robert C. Martin'
    },
    {
        'id': 2,
        'titulo': 'Entendendo Algoritmos: Um Guia Ilustrado Para Programadores e Outros Curiosos.',
        'autor': 'Aditya Y. Bhargava'
    },
    {
        'id': 3,
        'titulo': 'A Sutil Arte de Ligar o F*da-Se: Uma estrategia inusitada para uma vida melhor',
        'autor': 'Mark Manson'
    },
]

# Consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)