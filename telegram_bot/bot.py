import requests
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
bot_token = config["telegram"]["bot_token"]
chat_id = config["telegram"]["chat_id"]

def send_telegram_signal(signal):
    message = (
        f"📢 <b>Новый сигнал</b>\n"
        f"📊 Пара: <b>{signal['pair']}</b>\n"
        f"📈 Направление: <b>{signal['side'].upper()}</b>\n"
        f"🎯 Вход: {signal['entry']:.2f}\n"
        f"💰 TP: {signal['take_profit']:.2f}\n"
        f"🛑 SL: {signal['stop_loss']:.2f}\n"
        f"⚖️ Плечо: {signal['leverage']}x\n"
        f"✅ Уверенность: {signal['confidence'] * 100:.1f}%"
    )
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, data=payload)
