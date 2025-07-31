# 🤖 Bot Fiscal de Preço

Este é um bot simples em Python que monitora o preço de um produto em um link de um site de compra. Quando o preço cai abaixo de um valor definido, ele envia uma notificação automática via Telegram.

---

## 🚀 Funcionalidades

- Faz scraping do preço do produto no site da Kabum
- Converte o valor para float com precisão
- Compara com o preço-alvo definido
- Envia alerta via Telegram quando o preço estiver abaixo ou igual ao desejado
- Loop contínuo com verificação periódica (ex: a cada 1 hora)

---

## 🧠 Pré-requisitos

- Python 3.9+
- Conta e bot configurado no Telegram
- ID do seu chat (usando [@userinfobot](https://t.me/userinfobot))

---

## 📦 Instalação

1. Clone este repositório:

git clone https://github.com/seu-usuario/bot-preco.git

cd bot-preco

---

Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
venv\Scripts\activate    # Windows

ou

source venv/bin/activate # Linux/macOS

---

Instale as dependências:

pip install -r requirements.txt

---

🛠️ Configuração
Edite o arquivo main.py com as seguintes informações:

TOKEN = 'SEU_TOKEN_DO_BOT'
CHAT_ID = 1234567890
URL = 'LINK_DO_PRODUTO_KABUM'
PRECO_ALVO = 2500

---

▶️ Execução
Basta rodar o script principal:

python main.py

---

O bot irá rodar em loop e verificar o preço periodicamente.

---

📄 Estrutura de Arquivos

bot-preco/
│
├── scraper.py        # Função para extrair preço do site Kabum
├── main.py           # Script principal com lógica do bot
├── requirements.txt  # Dependências do projeto
└── README.md         # Este arquivo


🛡️ Aviso de Segurança
Nunca compartilhe seu TOKEN ou CHAT_ID publicamente. Use variáveis de ambiente ou arquivos .env em produção (recomendado).

📬 Licença
Este projeto é open-source e está disponível sob a licença MIT.