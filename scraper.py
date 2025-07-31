import requests
from bs4 import BeautifulSoup

def obter_preco_kabum(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    resposta = requests.get(url, headers=headers)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')

        preco_elemento = soup.find('h4', class_='text-4xl text-secondary-500 font-bold transition-all duration-500')  # Classe do preço no Kabum
        if preco_elemento:
            preco = preco_elemento.text.strip()
            return preco
        else:
            return "Preço não encontrado!"
    else:
        return f"Erro ao acessar página: {resposta.status_code}"


# Teste:
url = "https://www.kabum.com.br/produto/589244/ar-condicionado-split-parede-springer-midea-xtreme-save-connect-inverter-9-000-btu-h-qf-r32-220v-1f"
print("💰 Preço atual:", obter_preco_kabum(url))
