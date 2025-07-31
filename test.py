import asyncio
from telegram import Bot

TOKEN = '8413101602:AAEbp7n8quk5JOF8F5nI7q6pda41z0jYySU'
CHAT_ID = 6537532335  # Substitua aqui

async def main():
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="✅ Bot funcionando! Mensagem recebida com sucesso.")

asyncio.run(main())