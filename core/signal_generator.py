from core.data_collector import get_klines
from core.indicators import add_indicators
import random

def generate_best_signal():
    pairs = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "ADAUSDT", "DOGEUSDT", "AVAXUSDT", "LTCUSDT", "BNBUSDT", "MATICUSDT"]
    best_signal = None
    max_confidence = 0

    for pair in pairs:
        df = get_klines(pair)
        df = add_indicators(df)
        if df.empty:
            continue

        rsi = df["rsi"].iloc[-1]
        if rsi < 30:
            signal = {
                "pair": pair,
                "side": "long",
                "entry": df['close'].iloc[-1],
                "stop_loss": df['close'].iloc[-1] * 0.98,
                "take_profit": df['close'].iloc[-1] * 1.03,
                "leverage": 10,
                "confidence": round(random.uniform(0.8, 0.9), 3)
            }
        elif rsi > 70:
            signal = {
                "pair": pair,
                "side": "short",
                "entry": df['close'].iloc[-1],
                "stop_loss": df['close'].iloc[-1] * 1.02,
                "take_profit": df['close'].iloc[-1] * 0.97,
                "leverage": 10,
                "confidence": round(random.uniform(0.8, 0.9), 3)
            }
        else:
            continue

        if signal["confidence"] > max_confidence:
            best_signal = signal
            max_confidence = signal["confidence"]

    return best_signal
