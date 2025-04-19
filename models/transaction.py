from core.utils import get_current_date, to_decimal
from config import MAKER_FEE_RATE, TAKER_FEE_RATE


class Transaction:
    """
    Represents a single trading transaction (buy or sell) for a specific coin,
    including fee and total cost calculation in USDT.
    """

    def __init__(self, type, coin, quantity, price):
        """
        Initializes transaction data: type, coin, quantity, price.
        Automatically calculates fee and total cost.
        """
        self.date = get_current_date()
        self.type = type
        self.coin = coin
        self.quantity = to_decimal(quantity)
        self.price = to_decimal(price)
        self.fee = self.calculate_maker_fee() if self.type == "buy" else self.calculate_taker_fee()
        self.total_cost = self.calculate_total_cost()

    def calculate_maker_fee(self):
        """
        Calculates maker fee (for buy transactions).
        The fee is deducted from the quantity and adjusted.
        """
        maker_fee = self.quantity / (1 - to_decimal(MAKER_FEE_RATE)) - self.quantity
        return maker_fee

    def calculate_taker_fee(self):
        """
        Calculates taker fee (for sell transactions).
        Taken from the total return in USDT.
        """
        taker_fee = self.quantity * self.price * to_decimal(TAKER_FEE_RATE)
        return taker_fee

    def calculate_total_cost(self):
        """
        Calculates total USDT after applying the fee:
        - For buys: add the fee (converted to USDT).
        - For sells: subtract the fee from total.
        """
        total_cost = self.quantity * self.price
        return total_cost + (self.fee * self.price) if self.type == "buy" else total_cost - self.fee
