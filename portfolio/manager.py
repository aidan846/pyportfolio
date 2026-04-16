import json
from pathlib import Path

# Saving and Loading JSON
def load_portfolio():
    try:
        with open("data/portfolio.json", 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found")
        quit()

def save_portfolio(data):
    with open("data/portfolio.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)



# Position Management
def add_position(ticker, shares, price):
    data = load_portfolio()

    new_entry = {
        "ticker": ticker.upper(),
        "shares": shares,
        "avg_price": price
    }

    data["investments"].append(new_entry)
    save_portfolio(data)

def remove_position(ticker, shares_to_remove, sell_price):
    data = load_portfolio()
    ticker = ticker.upper()

    current_cash = float(data["cash-bal"])
    gain = shares_to_remove * sell_price
    data["cash-bal"] = str(current_cash + gain)

    for i, inv in enumerate(data["investments"]):
        if inv["ticker"] == ticker:
            if inv["shares"] > shares_to_remove:
                # Still have shares left, just subtract
                inv["shares"] -= shares_to_remove
            else:
                # Removing all shares, so delete the ticker from the list
                data["investments"].pop(i)
            break 
    
    save_portfolio(data)

def set_cash_bal(cash):
    data = load_portfolio()
    data["cash-bal"] = str(cash)
    save_portfolio(data)