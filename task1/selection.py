"""
Demonstrates if/elif/else and match-case selection statements.
Requires Python 3.10+ for match-case.
"""


def grade_with_if(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    return "D"


def day_type_with_match(day: str) -> str:
    match day.lower():
        case "saturday" | "sunday":
            return "Weekend"
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case _:
            return "Unknown"



print("Score 86 ->", grade_with_if(86))
print("Day Sunday ->", day_type_with_match("Sunday"))
