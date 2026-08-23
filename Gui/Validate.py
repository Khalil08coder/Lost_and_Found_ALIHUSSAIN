
import re
from datetime import datetime
from constants import MAX_NAME_LENGTH

# Item names may contain letters, numbers, spaces, and a small set of
# common punctuation.
NAME_PATTERN = re.compile(r"^[A-Za-z0-9 .,'-]+$")


def validate_item_name(name):
    """Checks an item name against the length and character rules.

    Returns true if the name is valid, or false
    """
    if name == "":
        return False, "Please enter the item name."

    if len(name) > MAX_NAME_LENGTH:
        return False, (
            f"Item name must be {MAX_NAME_LENGTH} characters or fewer."
        )

    if not NAME_PATTERN.match(name):
        return False, (
            "Item name can only contain letters, numbers, spaces, "
            "and basic punctuation (.,'-)."
        )

    return True, ""


def validate_not_future_date(parsed_date):
    """Rejects dates later than today
    parsed_date is a datetime object. Returns true if the date
    is today or earlier, or false if it's in the future.
    """
    if parsed_date.date() > datetime.now().date():
        return False, "Date cannot be in the future."

    return True, ""
