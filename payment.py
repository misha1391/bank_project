from card import *
from getCurrentTime import GetCurrentTime

class Payment:
    def __init__(self, amount: float, card: Card, merchant: str):
        self.amount = amount
        self.card = card
        self.merchant = merchant
        self.date = GetCurrentTime()
        self.success: bool = None
    def process(self) -> bool:
        self.success = self.card.pay(self.amount)
        return self.success