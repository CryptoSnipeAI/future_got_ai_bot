from pybit.unified_trading import HTTP
import pandas as pd

def get_klines(symbol, interval='15', limit=200, api_key='', api_secret=''):
    session = HTTP(api_key=api_key, api_secret=api_secret)
    res = session.get_kline(
        category="linear",
        symbol=symbol,
        interval=interval,
        limit=limit
    )
    data = res['result']['list']
    df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume", "turnover"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit='ms')
    df = df.astype({"open": float, "high": float, "low": float, "close": float, "volume": float})
    return df
