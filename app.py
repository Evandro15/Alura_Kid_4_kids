from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['video']
    name = request.form['name']
    literature_style = request.form['literature_style']
    
    # Salvar o arquivo no servidor
    uploaded_file.save(os.path.join('uploads', uploaded_file.filename))
    
    # Processar os dados como desejar
    
    #chama codigo do LLM, PASSANDO O NOME DA PESSOA E O ESTILO DE LITERATURA
    #TODO
    
    # Enviar o arquivo HTML para o cliente
    return send_file("C:\\Users\\eacorreia\\Desktop\\Imersao_Alura\\uploads\\testevideo.html", as_attachment=False)
    
    
    #return 'Dados recebidos com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
