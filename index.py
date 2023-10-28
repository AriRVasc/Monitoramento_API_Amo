import requests
import json
import time

# URL da API
api_url = 'https://brisa-ts.dev.amo.delivery/api/abc123'

while True:
    try:
        # Faça a solicitação GET à API
        response = requests.get(api_url)
        response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

        # Analisa a resposta JSON
        data = response.json()

        # Obtenha o último item da lista de dados
        last_item = data['data'][-1]

        # Exiba o último envio na tela
        print("ID:", last_item['_id'])
        print("Microcontroller Code:", last_item['microcontroller_code'])
        print("Temperature Int:", last_item.get('temperature_int', 'N/A'))
        print("Humidity Int:", last_item.get('humidity_int', 'N/A'))
        print("Temperature Ext:", last_item.get('temperature_ext', 'N/A'))
        print("Humidity Ext:", last_item.get('humidity_ext', 'N/A'))
        print("Created At:", last_item['created_at'])
        print("\n")

        # Aguarde um período antes de buscar novamente (por exemplo, 10 segundos)
        time.sleep(10)
    except requests.exceptions.RequestException as e:
        print("Erro ao buscar dados da API:", e)
    except json.JSONDecodeError as e:
        print("Erro ao analisar a resposta JSON:", e)
