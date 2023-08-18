import numpy as np
import random
from nltk.stem.lancaster import LancasterStemmer
from converting_input_to_numpy_array import bag_of_words
from training_the_model import model
from preprocessing_json_file import labels
from preprocessing_json_file import data
from preprocessing_json_file import words
from Smart_Nanny.SmartNanny_chatbot.connecting_chatbot_to_database.placing_order import checking_nanny_availability

stemmer = LancasterStemmer()


# prompts user for prompt to be used in the chatbot
def chat(text):
    inp = text

    # takes in input from user passes it into the function bag_of_words
    results = model.predict([bag_of_words(inp, words)])[0]

    # takes back the prediction with the highest probability
    results_index = np.argmax(results)

    # finds the tag with matching probability
    tag = labels[results_index]

    # only allows prediction with a 70% chance to be passed to the user any fewer passes an alternate response
    if results[results_index] > 0.7:
        for tg in data["intents"]:
            if tg["tag"] == "days_for_nanny_once_a_week_plan":
                response = checking_nanny_availability(text)
                return response
            elif tg["tag"] == tag:
                responses = tg["responses"]
                return random.choice(responses)
    else:
        return "I'm not sure I understood fully what you meant by that. Please ask me something else or is there " \
               "something else I could help you with?"


text = "I want them to come on Saturday"
response = chat(text)
print(response)
