import time
from portfolio.calculations import percent_pl, total_pl
from portfolio.manager import load_portfolio
from services.price_fetcher import fetch_price_snapshot
from ui.display import show_portfolio

from rich.live import Live


def build_display_rows(portfolio_data, price_snapshot):
	rows = []

	for position in portfolio_data.get("investments", []):
		ticker = position["ticker"].upper()
		shares = float(position["shares"])
		avg_price = float(position["avg_price"])

		quote = price_snapshot.get(ticker)
		if quote:
			current_price = quote["current_price"]
			prev_close = quote["prev_close"]
		else:
			current_price = avg_price
			prev_close = avg_price

		daily_pl_dollar = (current_price - prev_close) * shares
		daily_pl_percent = ((current_price - prev_close) / prev_close) * 100 if prev_close else 0.0
		total_pl_dollar = total_pl(current_price, avg_price, shares)
		total_pl_percent = percent_pl(current_price, avg_price)

		rows.append(
			{
				"ticker": ticker,
				"shares": shares,
				"price": current_price,
				"daily_pl_dollar": daily_pl_dollar,
				"daily_pl_percent": daily_pl_percent,
				"total_pl_dollar": total_pl_dollar,
				"total_pl_percent": total_pl_percent,
			}
		)

	return rows


def main():
	portfolio_data = load_portfolio()
	tickers = [position["ticker"].upper() for position in portfolio_data.get("investments", [])]
	price_snapshot = fetch_price_snapshot(tickers)
	display_rows = build_display_rows(portfolio_data, price_snapshot)
	show_portfolio(display_rows)

if __name__ == "__main__":
    # 'live' context manager handles screen refreshing
    with Live(main(), refresh_per_second=0.5) as live:
        while True:
            time.sleep(5) # Update once per second
            live.update(main())