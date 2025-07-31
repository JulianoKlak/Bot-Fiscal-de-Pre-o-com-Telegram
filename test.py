import asyncio
from telegram import Bot

TOKEN = 'SEU_TOKEN_DO_BOT'
CHAT_ID = SEU_CHAT_ID  

async def main():
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="✅ Bot funcionando! Mensagem recebida com sucesso.")

asyncio.run(main())