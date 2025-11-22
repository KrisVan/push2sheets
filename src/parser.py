import re

def parse_expense(text: str):
    """
    Parses raw notification text and returns a structured expense dictionary.
    Example input: "You spent $12.50 at Starbucks"
    Returns: {"amount": 12.50, "merchant": "Starbucks", "raw": text}
    """

    # Extract the amount with a regex
    amount_match = re.search(r"\$([\d\.]+)", text)
    if not amount_match:
        return None

    amount = float(amount_match.group(1))

    # Extract the merchant name
    merchant_match = re.search(r"at ([\w\s\.\-&]+)", text)
    merchant = merchant_match.group(1) if merchant_match else "Unknown"

    return {
        "amount": amount,
        "merchant": merchant,
        "raw": text
    }