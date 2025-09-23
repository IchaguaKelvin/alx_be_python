# weather_advice.py
# Weather Recommendation Program
# This program asks users about weather conditions and provides clothing recommendations

def main():
    print("=== Weather Clothing Recommendation System ===")
    print()
    
    # Prompt user for weather input
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower().strip()
    
    # Provide clothing recommendations based on weather conditions
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

# Run the program
if __name__ == "__main__":
    main()