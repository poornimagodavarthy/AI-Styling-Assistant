from evolutionary import evolutionary_algorithm, comparison
from user_inputs import quiz
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'gender': ['Male', 'Female'],
    'baseColour': ['Red', 'Blue'],
    'season': ['Summer', 'Winter'],
    'usage': ['Casual', 'Formal']
})

# Get user preferences from quiz function
user_preferences = quiz(df)  

attribute_weights = {
    'gender': 1,
    'baseColour': 3,
    'season': 2,
    'usage': 2
}


best_recommendation = evolutionary_algorithm(user_preferences, attribute_weights)
top, bottom = comparison(best_recommendation)

def retrieve_image(best_id):
    image_name = str(best_id) + '.jpg'  # Ensure best_id is converted to string
    image_path = 'drive/MyDrive/fashion-dataset/images/' + image_name
    image = Image.open(image_path)
    plt.imshow(image)
    plt.axis('off')
    plt.show()

retrieve_image(top)
retrieve_image(bottom)
print("Best recommendation:", top, bottom)

satisfied = int(input("Rank your overall satisfaction with your recommendation out of 10: "))

while satisfied <= 6:
    gender_satisfaction = int(input("Rank your satisfaction of your recommendation's gender match out of 5: "))
    colour_satisfaction = int(input("Rank your satisfaction of your recommendation's base colour out of 5: "))
    season_satisfaction = int(input("Rank your satisfaction of your recommendation's season out of 5: "))
    usage_satisfaction = int(input("Rank your satisfaction of your recommendation's usage out of 5: "))

    attribute_weights['gender'] += (5 - gender_satisfaction)
    attribute_weights['baseColour'] += (5 - colour_satisfaction)
    attribute_weights['season'] += (5 - season_satisfaction)
    attribute_weights['usage'] += (5 - usage_satisfaction)

    best_recommendation = evolutionary_algorithm(user_preferences, attribute_weights)
    top, bottom = comparison(best_recommendation)
    retrieve_image(top)
    retrieve_image(bottom)
    print("Best recommendation:", top, bottom)

    satisfied = int(input("Rank your overall satisfaction with your recommendation out of 10: "))

