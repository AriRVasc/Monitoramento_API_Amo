from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

# URL da API
api_url = 'https://brisa-ts.dev.amo.delivery/api/abc123'

@app.route('/')
def index():
    try:
        # Faça a solicitação GET à API
        response = requests.get(api_url)
        response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

        # Analisa a resposta JSON
        data = response.json()

        # Obtenha o último item da lista de dados
        last_item = data['data'][-1]

        # Renderiza a página HTML com os dados
        return render_template('index.html', last_item=last_item)
    except requests.exceptions.RequestException as e:
        return f"Erro ao buscar dados da API: {e}"
    except json.JSONDecodeError as e:
        return f"Erro ao analisar a resposta JSON: {e}"

if __name__ == '__main__':
    app.run(debug=True)
