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
        self.quantity = Decimal(str(quantity))
        self.price = Decimal(str(price))
        self.fee = _round(self.calc_fee(), 8)
        self.total_cost = _round(self.calc_total_cost(), 2)

    def calc_fee(self):
        """
        Calculates the transaction fee based on type and FEES_RATE.
        
        Returns:
            Decimal: The calculated fee.
        """
        if self.type.lower() == "buy":
            fees_percentage = Decimal(str(FEES_RATE)) * Decimal('100')
            net_percentage = Decimal('100') - fees_percentage
            fees_from_quantity = ((self.quantity * Decimal('100')) / net_percentage) - self.quantity
            return fees_from_quantity
        return self.quantity * self.price * Decimal(str(FEES_RATE))

    def calc_total_cost(self):
        """
        Calculates the total USDT involved in the transaction after fees.
        
        Returns:
            Decimal: The total USDT amount (cost for buys, return for sells).
        """
        total_cost = self.quantity * self.price
        if self.type.lower() == "buy":
            return total_cost + (self.fee * self.price) # <- here before edit total_cost + (self.fee * self.price)
        return total_cost - self.fee
