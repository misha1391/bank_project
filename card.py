from account import BankAccount

class Card:
    def __init__(self, card_number: str, expiry_date: str, account: BankAccount):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.account = account
    def get_balance(self) -> float:
        return self.account.balance
    def pay(self, amount: float) -> bool:
        if amount > self.get_balance():
            return False
        else:
            self.account.withdraw(amount)
            return True

class DebitCard(Card):
    def __init__(self, card_number: str, expiry_date: str, account: BankAccount):
        super().__init__(card_number, expiry_date, account)
class CreditCard(Card):
    def __init__(self, card_number: str, expiry_date: str, account: BankAccount, credit_limit: float):
        super().__init__(card_number, expiry_date, account)
        self.credit_limit = credit_limit
        self.debt = 0.0
    def pay(self, amount: float) -> bool:
        balance = self.get_balance()
        if amount > balance:
            self.debt += amount - balance
            self.account.withdraw(balance)
        else:
            self.account.withdraw(amount)
        return True