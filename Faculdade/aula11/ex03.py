import requests

# URL da API de câmbio do Banco Central do Brasil
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json"

try:
    # Fazendo uma solicitação GET para a API
    response = requests.get(url)

    # Verifica se a solicitação foi bem-sucedida (código 200)
    if response.status_code == 200:
        # Converte a resposta JSON em um dicionário
        data = response.json()

        # Extrai o valor da cotação do dólar mais recente
        cotacao_dolar = data[-1]["valor"]

        # Imprime o valor da cotação do dólar
        print(f"O valor da cotação do dólar é: R$ {cotacao_dolar}")
    else:
        print("Falha na solicitação à API.")
except Exception as e:
    print(f"Erro: {e}")
