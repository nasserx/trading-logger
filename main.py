from models.transaction import Transaction
from core.utils import is_number, data_format
from core.logger import save_to_csv
from config import TYPES, CSV_PATH, HEADERS


def main():
    while True:
        type = input("Transaction type (buy or sell): ")
        coin = input("Coin name: ")
        quantity = input("Quantity: ")
        price = input("Price: ")

        if type.lower() not in TYPES:
            print("Invalid value. Please use only 'buy' or 'sell'.")
            continue
        check_inputs = all(is_number(v) for v in (quantity, price))
        if not check_inputs:
            print("Invalid Value. Quantity and price must be numbers")
            continue

        transaction = Transaction(type, coin, quantity, price)
        dformat = [data_format(transaction)]
        save_to_csv(CSV_PATH, HEADERS, dformat)

        answer = input("Do you want to add another transaction? (Y/N): ")
        if answer.upper() != "Y":
            break

        


if __name__ == "__main__":
    main()
