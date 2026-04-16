import yfinance as yf


def fetch_price_snapshot(tickers):
    snapshot = {}

    for ticker in tickers:
        try:
            history = yf.Ticker(ticker).history(period="5d", interval="1d", auto_adjust=False)
            closes = history["Close"].dropna()

            if closes.empty:
                continue

            current_price = float(closes.iloc[-1])
            prev_close = float(closes.iloc[-2]) if len(closes) > 1 else current_price

            snapshot[ticker] = {
                "current_price": current_price,
                "prev_close": prev_close,
            }
        except Exception:
            # Skip tickers that fail to fetch to keep the app responsive.
            continue

    return snapshot