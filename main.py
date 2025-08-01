import asyncio
from telegram import Bot
from scraper import obter_preco_kabum

TOKEN = 'SEU_TOKEN_DO_BOT' # Substitua pelo seu token
CHAT_ID = SEU_CHAT_ID # Substitua pelos valores corretos
URL = "https://www.kabum.com.br/produto/589244/ar-condicionado-split-parede-springer-midea-xtreme-save-connect-inverter-9-000-btu-h-qf-r32-220v-1f"
PRECO_ALVO = 1999.0  # usar ponto, não usar vírgula

bot = Bot(token=TOKEN)

def converter_preco(preco_str):
    preco_limpo = preco_str.replace("R$", "").replace(".", "").replace(",", ".").strip()
    preco = float(preco_limpo)
    # print(f"[DEBUG] Preço convertido para float: {preco} | Tipo: {type(preco)}")
    # print(f"[DEBUG] Comparando com preço-alvo: {PRECO_ALVO}")
    return preco

async def checar_preco():
    preco_str = obter_preco_kabum(URL)
    print("Preço atual:", preco_str)

    if "R$" in preco_str:
        preco = converter_preco(preco_str)

        if preco <= PRECO_ALVO:
            mensagem = f"📉 O preço caiu! Agora está {preco_str}!\n\n👉 {URL}"
            await bot.send_message(chat_id=CHAT_ID, text=mensagem)
        else:
            print("Preço ainda alto. Nada enviado.")
    else:
        print("❌ Erro ao capturar preço:", preco_str)

async def main():
    while True:
        await checar_preco()
        await asyncio.sleep(3600)  # espera 1 hora

asyncio.run(main())
# asyncio.run(checar_preco())
