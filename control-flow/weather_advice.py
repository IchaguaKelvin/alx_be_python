# 1. Prompt User for Weather Input
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# 2. Provide Clothing Recommendations
if weather == "sunny":
    recommendation = "wear a t-shirt and sunglasses."
elif weather == "rainy":
    recommendation = "don't forget your umbrella and a raincoat."
elif weather == "cold":
    recommendation = "make sure to wear a warm coat and a scarf."
else:
    recommendation = "Sorry, I don't have recommendations for this weather."

# 3. Output the Recommendation
print(recommendation)
