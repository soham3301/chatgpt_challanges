
from dataclasses import dataclass

@dataclass
class Food:
    name: str
    price: int
    quantity: int = 0
