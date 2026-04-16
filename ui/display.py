from rich.table import Table
from rich.console import Console
from rich import box

console = Console()

def show_portfolio(data):
    console.clear() 
    table = Table(title="📊 Portfolio", box=box.ROUNDED)

    table.add_column("Ticker")
    table.add_column("Shares", justify="right")
    table.add_column("Price", justify="right")
    table.add_column("Daily P/L $", justify="right")
    table.add_column("Daily P/L %", justify="right")
    table.add_column("Total P/L $", justify="right")
    table.add_column("Total P/L %", justify="right")

    for pos in data:
        daily_color = "green" if pos["daily_pl_dollar"] >= 0 else "red"
        total_color = "green" if pos["total_pl_dollar"] >= 0 else "red"

        table.add_row(
            pos["ticker"],
            f"{pos['shares']:.2f}",
            f"${pos['price']:.2f}",
            f"[{daily_color}]${pos['daily_pl_dollar']:.2f}[/{daily_color}]",
            f"[{daily_color}]{pos['daily_pl_percent']:.2f}%[/{daily_color}]",
            f"[{total_color}]${pos['total_pl_dollar']:.2f}[/{total_color}]",
            f"[{total_color}]{pos['total_pl_percent']:.2f}%[/{total_color}]",
        )

    console.print(table)