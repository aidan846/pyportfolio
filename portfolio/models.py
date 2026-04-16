from dataclasses import dataclass

@dataclass
class Position:
    ticker: str
    shares: float
    avg_price: float