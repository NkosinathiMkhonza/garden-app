"""
Garden Advice App
A simple application that provides gardening tips based on the month and season.
"""

def get_gardening_advice(month, season):
    # TODO: Add input validation for month and season parameters
    # TODO: Consider using a dictionary for advice storage instead of hardcoded values
    
    advice = ""
    
    # Spring advice
    if season == "spring":
        # TODO: Create a separate function for spring advice
        if month in ["September", "October", "November"]:
            advice = "Spring is here! Time to plant new seeds and prepare your garden beds."
        else:
            advice = "Check if the month matches the season."
    
    # Summer advice
    elif season == "summer":
        # TODO: Create a separate function for summer advice
        if month in ["December", "January", "February"]:
            advice = "Summer is hot! Remember to water your plants regularly and provide shade."
        else:
            advice = "Check if the month matches the season."
    
    # Autumn advice
    elif season == "autumn":
        # TODO: Create a separate function for autumn advice
        if month in ["March", "April", "May"]:
            advice = "Autumn is perfect for harvesting and preparing plants for winter."
        else:
            advice = "Check if the month matches the season."
    
    # Winter advice
    elif season == "winter":
        # TODO: Create a separate function for winter advice
        if month in ["June", "July", "August"]:
            advice = "Winter is cold! Protect your plants from frost and reduce watering."
        else:
            advice = "Check if the month matches the season."
    
    else:
        advice = "Invalid season. Please enter spring, summer, autumn, or winter."
    
    return advice


# TODO: Add a main function to run the program
# TODO: Add user input handling
# TODO: Add docstrings to all functions

def main():
    print("Welcome to the Garden Advice App!")
    print("=" * 40)
    
    # TODO: Replace hardcoded values with user input
    month = input("Enter the current month: ")
    season = input("Enter the current season (spring, summer, autumn, winter): ")
    
    advice = get_gardening_advice(month, season)
    print("\nGardening Tip:", advice)


if __name__ == "__main__":
    main()
