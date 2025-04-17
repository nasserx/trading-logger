from decimal import Decimal
from config import FEES_RATE
from core.utils import get_current_date, _round

class Transaction:
    """
    Represents a trading transaction for a specific coin.
    
    Attributes:
        date (str): The date of the transaction.
        type (str): The type of transaction ("buy" or "sell").
        coin (str): The name or symbol of the coin.
        quantity (Decimal): The amount of the coin traded.
        price (Decimal): The price per coin in USDT.
        fee (Decimal): The calculated transaction fee.
        total_usdt (Decimal): The total cost or return in USDT.
    """

    def __init__(self, type, coin, quantity, price):
        """
        Initializes a new Transaction instance.
        
        Args:
            type (str): The transaction type ("buy" or "sell").
            coin (str): The coin symbol or name.
            quantity (float or str): The quantity of the coin.
            price (float or str): The price per unit of the coin.
        """
        self.date = get_current_date()
        self.type = type
        self.coin = coin
        self.quantity = Decimal(quantity)
        self.price = Decimal(price)
        self.fee = self.get_maker_fee() if self.type == "buy" else self.get_taker_fee()
        self.total_cost = self.get_total_cost()

    def get_maker_fee(self):
        """
        Calculates the fee for a 'buy' transaction.
        The fee is deducted from the quantity, so we adjust to find the actual fee amount.

        Returns:
            Decimal: The fee in coin units, rounded to 8 decimal places.
        """
        maker_fee = self.quantity / (1 - Decimal(FEES_RATE)) - self.quantity
        return _round(maker_fee, 8)

    def get_taker_fee(self):
        """
        Calculates the fee for a 'sell' transaction.
        The fee is taken from the total USDT amount (quantity * price).

        Returns:
            Decimal: The fee in USDT, rounded to 8 decimal places.
        """
        taker_fee = self.quantity * self.price * Decimal(FEES_RATE)
        return _round(taker_fee, 8)

    def get_total_cost(self):
        """
        Calculates the total USDT involved in the transaction after fees.
        For 'buy' transactions, the fee is converted to USDT (fee * price).
        For 'sell' transactions, the fee is already in USDT and added to the total.

        Returns:
            Decimal: The total USDT amount (cost for buys, return for sells).
        """
        total_cost = self.quantity * self.price
        if self.type.lower() == "buy":
            return total_cost + (self.fee * self.price)
        return total_cost - self.fee
