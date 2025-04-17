from decimal import Decimal, ROUND_HALF_UP
import datetime

def get_current_date():
    """
    Returns the current date as a string in the format YYYY-MM-DD.
    
    Returns:
        str: The current date.
    """
    return datetime.date.today().strftime("%Y-%m-%d")


def _round(value: Decimal, decimals=2):
    """
    Performs standard rounding (round-half-up) using the Decimal module for precision.

    This function rounds a Decimal value to a specified number of decimal places using
    the round-half-up method, which is the most commonly used rounding strategy in financial
    and general arithmetic contexts.

    Parameters:
        value (Decimal): The numeric value to be rounded. Must be a Decimal object.
        decimals (int): The number of decimal places to round to (default is 2).

    Returns:
        Decimal: The rounded value as a Decimal object with the specified precision.

    Example:
        _round(Decimal('2.675'), 2)     -> Decimal('2.68')
        _round(Decimal('123.4567'), 1) -> Decimal('123.5')
    """
    quantizer = Decimal('1.' + '0' * decimals)
    return value.quantize(quantizer, rounding=ROUND_HALF_UP)


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
        f"{obj.fee} {obj.coin.upper()}" if obj.type == "buy" else f"{obj.fee} $",
        f"{obj.total_cost}$"
    ]
