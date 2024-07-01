
user_preferences = {}

def quiz(df):
    print("Please answer the following questions to personalize your styling experience.")

    gender_options = df['gender'].unique().tolist()
    baseColour_options = df['baseColour'].unique().tolist()
    season_options = df['season'].unique().tolist()
    usage_options = df['usage'].unique().tolist()

    print("Gender options:", gender_options)
    user_preferences['gender'] = [input("What gender do you identify as? ").lower()]

    print("Base Colour options:", baseColour_options)
    user_preferences['baseColour'] = [input("What is your preferred base colour? ").lower()]

    print("Season options:", season_options)
    user_preferences['season'] = [input("What is your preferred season? ").lower()]

    print("Usage options:", usage_options)
    user_preferences['usage'] = [input("What is your preferred usage? ").lower()]

    print("Thank you for completing this quiz!")
    return user_preferences