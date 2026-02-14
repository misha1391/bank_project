from typing import List
from payment import *

is_testing = True # Для быстрой проверки

accounts: List[BankAccount] = []
cards: List[Card] = []
payment_history: List[Payment] = []

if is_testing:
    accounts.append(BankAccount(1, "Vlad"))
    cards.append(CreditCard("88005553535", "12/27", accounts[0], 1000.0))
    cards.append(DebitCard("88005553534", "12/27", accounts[0]))
    accounts[0].deposit(1000.0)

def createAcc():
    print("createAcc")
    while True:
        owner = input("Введите имя владельца: ")
        if not owner in [acc.owner for acc in accounts]:
            break
        print("Такое имя владельца уже занято")
    id = max([acc.account_number for acc in accounts]) + 1
    accounts.append(BankAccount(id, owner))
def createCard():
    print("createCard")
    while True:
        account = input("Введите аккаунт для привязки: ")
        if account in [acc.owner for acc in accounts]:
            break
        print("Нет такого владельца!")
    card_type = 0
    
    while True:
        print("Какой тип карты нужно выпустить?")
        print("1) Дебитовая")
        print("2) Кредитная")
        card_type = int(input())
        if 1 <= card_type <= 2:
            break
        print("Вы инвалид")
    
    card_number = input("Введите номер карты: ")
    while True:
        expiry_date = input("Введите срок действия карты(формат: мм/гг): ")
        month, year = expiry_date.split("/")
        if 1 >= month >= 12 and 26 >= year >= 99:
            break
        print("Вы инвалид")
    for acc in accounts:
        if acc.owner == account:
            if card_type == 1:
                cards.append(DebitCard(card_number, expiry_date, acc))
            else:
                cards.append(CreditCard(card_number, expiry_date, acc))
            break
def depositCard():
    print("depositCard")
    card_number = input("Введите номер карты: ")
    for card in cards:
        if card.card_number == card_number:
            amount = float(input("Введите количество денег для пополнения: "))
            card.account.deposit(amount)
            break
def payCard():
    print("payCard")
    card_number = input("Введите номер карты: ")
    for card in cards:
        if card.card_number == card_number:
            merchant = input("Введите название организации: ")
            amount = float(input("Введите количество денег для оплаты: "))
            payment_history.append(Payment(amount, card, merchant))
            success = payment_history[-1].process()
            print("Оплата произошла " + ("успешно" if success else "провально"))
            break
def default():
    print("Вы инвалид")

switch_case = {
    1: createAcc,
    2: createCard,
    3: depositCard,
    4: payCard,
    5: exit
}

while True:
    print("Что нужно сделать:")
    print("1) Создать аккаунт")
    print("2) Создать карту")
    print("3) Пополнить карту")
    print("4) Оплатить")
    print("5) Выйти из программы")
    answer = int(input())
    switch_case.get(answer, default)()