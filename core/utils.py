from decimal import Decimal, ROUND_HALF_UP
import datetime

def get_current_date():
    """
    Returns the current date as a string in the format YYYY-MM-DD.
    
    Returns:
        str: The current date.
    """
    return datetime.date.today().strftime("%Y-%m-%d")


def to_decimal(value: str, decimals: int = None):
    """
    Converts a value to a Decimal, with optional rounding to a specific number of decimal places.
    
    Args:
        value (str): The value to convert.
        decimals (int, optional): Number of decimal places to round to.
    
    Returns:
        Decimal: The converted decimal value.
    """
    d = Decimal(str(value))
    if decimals is not None:
        quantizer = Decimal(f"1.{'0'*decimals}")
        return d.quantize(quantizer, rounding=ROUND_HALF_UP)
    return d


def is_number(value):
    """
    Checks if the given value can be converted to a float.
    
    Args:
        value: The value to check.
    
    Returns:
        bool: True if the value is numeric, False otherwise.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def data_format(obj):
    """
    Formats transaction object data into a list of values for display or export.
    
    Args:
        obj: A transaction-like object with attributes (date, type, coin, quantity, price, fee, total_usdt).
    
    Returns:
        list: A list of formatted strings and values representing the transaction.
    """
    return [
        obj.date,
        obj.type.lower(),
        obj.coin.upper(),
        obj.quantity,
        f"{obj.price}$",
        f"{to_decimal(obj.fee, 6)}{obj.coin.upper()}" if obj.type == "buy" else f"{to_decimal(obj.fee, 2)}$",
        f"{to_decimal(obj.total_usdt, 2)}$"
    ]
