from decimal import Decimal, ROUND_HALF_UP
import datetime


def get_current_date():
    """
    Returns today's date in YYYY-MM-DD format.
    """
    return datetime.date.today().strftime("%Y-%m-%d")


def to_decimal(value: str):
    """
    Converts a string or number to Decimal.
    """
    return Decimal(value)


def dround(value: Decimal, decimals=2):
    """
    Rounds a Decimal to the given number of decimals (round-half-up).
    """
    quantizer = Decimal('1.' + '0' * decimals)
    return value.quantize(quantizer, rounding=ROUND_HALF_UP)


def is_numeric(value):
    """
    Checks if the value is numeric (float-compatible).
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def data_format(obj):
    """
    Formats a transaction object into a list for display or export.
    """
    return [
        obj.date,
        obj.type.lower(),
        obj.coin.upper(),
        obj.quantity,
        f"{obj.price}$",
        f"{dround(obj.fee, 8)} {obj.coin.upper()}" if obj.type == "buy" else f"{dround(obj.fee, 8)} $",
        f"{dround(obj.total_cost, 2)}$"
    ]
