"""
garden_advice.py

Provides gardening tips and advice based on the current month and season.
Designed for gardening enthusiasts around the world.
"""
#########so what now?, tell me what now 
# Season definitions mapping each month to its season
MONTH_TO_SEASON = {
    12: "Summer", 1: "Summer", 2: "Summer",       # Southern Hemisphere
    3: "Autumn", 4: "Autumn", 5: "Autumn",
    6: "Winter", 7: "Winter", 8: "Winter",
    9: "Spring", 10: "Spring", 11: "Spring"
}

# Gardening advice mapped by season
# Add docstrings to all functions to improve code documentation issue 2
SEASON_ADVICE = {
    "Summer": [
        "Water plants early in the morning to reduce evaporation.",
        "Apply mulch around plants to retain moisture.",
        "Watch out for pests — inspect leaves regularly.",
        "Harvest vegetables frequently to encourage more growth."
    ],
    "Autumn": [
        "Plant spring-flowering bulbs now.",
        "Rake fallen leaves and add them to your compost.",
        "Reduce watering as temperatures drop.",
        "Prune dead wood from trees and shrubs."
    ],
    "Winter": [
        "Protect frost-sensitive plants with fleece or mulch.",
        "Plan next year's garden layout.",
        "Order seeds from catalogues.",
        "Clean and sharpen your gardening tools."
    ],
    "Spring": [
        "Start sowing seeds indoors for transplanting later.",
        "Divide and replant overgrown perennials.",
        "Begin fertilising plants as growth resumes.",
        "Keep an eye on late frosts and protect young plants."
    ]
}

# Month names for display purposes
MONTH_NAMES = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}


def get_season(month):
    """
    Return the season for a given month number (Southern Hemisphere).

    Args:
        month (int): Month number (1-12).

    Returns:
        str: The season name, or None if the month is invalid.
    """
    return MONTH_TO_SEASON.get(month)


def get_advice(season):
    """
    Return a list of gardening tips for the given season.

    Args:
        season (str): Season name (e.g. 'Summer', 'Winter').

    Returns:
        list: A list of gardening tip strings.
    """
    return SEASON_ADVICE.get(season, [])


def get_month_input():
    """
    Prompt the user to enter a month number and validate the input.

    Returns:
        int: A valid month number between 1 and 12.
    """
    while True:
        try:
            month = int(input("Enter the month number (1-12): "))
            if 1 <= month <= 12:
                return month
            else:
                print("Please enter a number between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def display_advice(month):
    """
    Display the season and gardening advice for the given month.

    Args:
        month (int): Month number (1-12).
    """
    month_name = MONTH_NAMES.get(month, "Unknown")
    season = get_season(month)

    if not season:
        print(f"No season data available for month {month}.")
        return

    advice_list = get_advice(season)

    print(f"\n🌿 Gardening Advice for {month_name} ({season})")
    print("-" * 45)

    if advice_list:
        for tip in advice_list:
            print(f"  • {tip}")
    else:
        print("  No advice available for this season.")
    print()


def main():
    """
    Main entry point for the garden advice application.
    Prompts the user for a month and displays relevant gardening tips.
    """
    print("Welcome to the Garden Advice App! 🌱")
    month = get_month_input()
    display_advice(month)


if __name__ == "__main__":
    main()
