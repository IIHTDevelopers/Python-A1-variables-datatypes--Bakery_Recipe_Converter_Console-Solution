# recipe_converter.py

# Conversion constants
CUP_FLOUR_TO_GRAMS = 128  # 1 cup flour = 128 grams
CUP_SUGAR_TO_GRAMS = 200  # 1 cup sugar = 200 grams

def convert_flour_to_grams(cups):
    """Convert flour from cups to grams (1 cup = 128 grams)"""
    # Input validation - DO NOT MODIFY
    if not isinstance(cups, (int, float)) or cups <= 0:
        raise ValueError("Flour amount must be positive")
        
    # Convert cups of flour to grams
    grams = cups * CUP_FLOUR_TO_GRAMS
    return round(grams)

def convert_sugar_to_grams(cups):
    """Convert sugar from cups to grams (1 cup = 200 grams)"""
    # Input validation - DO NOT MODIFY
    if not isinstance(cups, (int, float)) or cups <= 0:
        raise ValueError("Sugar amount must be positive")
        
    # Convert cups of sugar to grams
    grams = cups * CUP_SUGAR_TO_GRAMS
    return round(grams)

# Main program - DO NOT MODIFY
if __name__ == "__main__":
    print("Welcome to Recipe Converter!")
    print("-" * 30)
    
    # Get input from user
    recipe_name = input("Enter recipe name: ")
    flour_cups = float(input("Enter flour (cups): "))
    sugar_cups = float(input("Enter sugar (cups): "))
    
    # Convert measurements
    flour_grams = convert_flour_to_grams(flour_cups)
    sugar_grams = convert_sugar_to_grams(sugar_cups)
    
    # Print results
    print("\nCONVERTED RECIPE:", recipe_name)
    print(f"Flour: {flour_grams}g")
    print(f"Sugar: {sugar_grams}g")