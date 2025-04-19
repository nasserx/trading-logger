from models.transaction import Transaction
from core.utils import is_numeric, data_format
from core.logger import save_to_csv
from config import TYPES, CSV_PATH, HEADERS


def get_transaction_type():
    while True:
        t_type = input("Transaction type (buy or sell): ").lower()
        if t_type in TYPES:
            return t_type
        print("Invalid type. Please enter 'buy' or 'sell'.")


def get_coin_name():
    while True:
        coin = input("Coin name: ").strip()
        if coin:
            return coin
        print("Invalid input. The symbol name must be greater than or equal to 1")


def get_numeric_input(prompt):
    while True:
        value = input(prompt).strip()
        if is_numeric(value):
            return value
        print("Invalid input. Please enter a numeric value.")


def confirm_transaction():
    confirmation = input("Are you sure you want to add this transaction? (y/n): ").lower()
    if confirmation == "y":
        return True
    return False


def get_user_confirmation():
    return input("Do you want to add another transaction? (y/n): ").strip().upper() == "Y"


def collect_transaction():
    t_type = get_transaction_type()
    coin = get_coin_name()
    quantity = get_numeric_input("Quantity: ")
    price = get_numeric_input("Price: ")
    return Transaction(t_type, coin, quantity, price)


def main():
    while True:
        transaction = collect_transaction()
        if not confirm_transaction():
            break

        save_to_csv(CSV_PATH, HEADERS, [data_format(transaction)])
        if not get_user_confirmation():
            break



if __name__ == "__main__":
    main()