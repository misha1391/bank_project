class BankAccount:
    def __init__(self, account_number: str, owner: str):
        self.account_number = account_number
        self.owner = owner
        self.balance = 0.0
    # Пополнить
    def deposit(self, amount: float) -> None:
        self.balance += amount
    # Снять
    def withdraw(self, amount: float) -> bool:
        self.balance -= amount