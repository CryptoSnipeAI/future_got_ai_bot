# Bybit AI Signal Bot

## Установка и запуск

1. Установи зависимости:
```bash
pip install -r requirements.txt
```

2. Заполни `config.yaml`:
```yaml
bybit:
  api_key: "ТВОЙ_BYBIT_API_KEY"
  api_secret: "ТВОЙ_BYBIT_API_SECRET"

telegram:
  bot_token: "ТВОЙ_BOT_TOKEN"
  chat_id: "ТВОЙ_CHAT_ID"
```

3. Запусти:
```bash
python scheduler.py
```

## Docker

```bash
docker build -t bybit-ai-bot .
docker run -d bybit-ai-bot
```
