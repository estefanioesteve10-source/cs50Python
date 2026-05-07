import sys
import requests

def main():
    # 1. Verifica se o argumento foi passado
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    # 2. Tenta converter o argumento para float
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # 3. Configurações da API
    # Substitua pela sua chave real do CoinCap
    api_key = "SUA_CHAVE_AQUI"
    url = f"https://api.coincap.io/v2/assets/bitcoin"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # 4. Faz a requisição à API
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Verifica se houve erro HTTP (404, 500, etc)

        # 5. Extrai o preço do JSON
        data = response.json()
        price_usd = float(data["data"]["priceUsd"])

        # 6. Calcula e formata o custo total
        total_cost = amount * price_usd
        print(f"${total_cost:,.4f}")

    except requests.RequestException:
        sys.exit("Error fetching data from API")
    except (KeyError, TypeError):
        sys.exit("Error parsing API response")

if __name__ == "__main__":
    main()
