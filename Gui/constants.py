"""
Shared constants that are used across multiple files in the app.

Putting these here in one place means I don't have to change them
in multiple places if I want to change them later. It also makes
the code easier to read, since you can see what the constants are
and what they are used for.
"""


# dropdown in both the Report and Found windows so users can't type in
# an invalid location.
LOCATIONS = [
    "Rutherford",
    "Snell",
    "Mansfield",
    "Upham",
    "Batten",
    "Hillary",
    "Te Kanawa",
    "Kupe",
]

# Shared fonts, so every Label/Entry across the app pulls from one place
# instead of repeating ("Arial", 12) or ("Arial", 18, "bold") everywhere.
FONT_LABEL = ("Arial", 12)
FONT_TITLE = ("Arial", 18, "bold")

# Named window sizes so the geometry only has to be changed here,
# not everywhere a window is opened.
MAIN_WINDOW_WIDTH = 560
MAIN_WINDOW_HEIGHT = 560
TABLE_WINDOW_SIZE = "650x400"
FORM_WINDOW_SIZE = "400x420"

# Derived value: the Combobox width is calculated from the longest
# location name instead of being a guessed literal like 22. This way,
# if a longer location is ever added to LOCATIONS, the dropdown
# automatically resizes to fit it instead of needing a manual update.
LOCATION_WIDTH = max(len(name) for name in LOCATIONS) + 4

MAX_NAME_LENGTH = 50
