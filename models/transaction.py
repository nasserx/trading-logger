from config import FEES_RATE
from core.utils import get_current_date, to_decimal

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
        self.quantity = to_decimal(quantity)
        self.price = to_decimal(price)
        self.fee = to_decimal(self.calc_fee())
        self.total_usdt = to_decimal(self.calc_total_usdt())

    def calc_fee(self):
        """
        Calculates the transaction fee based on type and FEES_RATE.
        
        Returns:
            Decimal: The calculated fee.
        """
        if self.type.lower() == "buy":
            return (((self.quantity * 100) / to_decimal((100 - FEES_RATE * 100))) - self.quantity)
        return self.quantity * self.price * to_decimal(FEES_RATE)

    def calc_total_usdt(self):
        """
        Calculates the total USDT involved in the transaction after fees.
        
        Returns:
            Decimal: The total USDT amount (cost for buys, return for sells).
        """
        if self.type.lower() == "buy":
            return self.quantity * self.price + self.fee
        return self.quantity * self.price - self.fee
