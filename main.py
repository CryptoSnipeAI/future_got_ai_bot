from core.signal_generator import generate_best_signal
from telegram_bot.bot import send_telegram_signal

def main():
    signal = generate_best_signal()
    if signal:
        send_telegram_signal(signal)

if __name__ == "__main__":
    main()
