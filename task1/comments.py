"""
Demonstrates single-line, inline, and docstring comments.
"""

# Single-line comment: this constant stores a tax rate.
TAX_RATE = 0.13


def calculate_total(price: float) -> float:
    """Return price including tax."""
    subtotal = price  # Inline comment: no discount applied.
    total = subtotal * (1 + TAX_RATE)
    return round(total, 2)


def explain_comments() -> None:
    # This message explains comment styles.
    print("Single-line comments start with #")
    print("Inline comments appear on the same line as code")
    print("Docstrings describe modules, classes, and functions")



explain_comments()
print(f"Total for 100.00 = {calculate_total(100.00)}")
