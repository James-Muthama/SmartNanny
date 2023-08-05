import numpy as np
import random
from nltk.stem.lancaster import LancasterStemmer
from converting_input_to_numpy_array import bag_of_words
from training_the_model import model
from preprocessing_json_file import labels
from preprocessing_json_file import data
from preprocessing_json_file import words

stemmer = LancasterStemmer()


# prompts user for prompt to be used in the chatbot
def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You:")
        if inp.lower() == "quit":
            break

        # takes in input from user passes it into the function bag_of_words
        results = model.predict([bag_of_words(inp, words)])[0]

        # takes back the prediction with the highest probability
        results_index = np.argmax(results)

        # finds the tag with matching probability
        tag = labels[results_index]

        # only allows prediction with a 70% chance to be passed to the user any less passes an alternate response
        if results[results_index] > 0.7:
            for tg in data["intents"]:
                if tg["tag"] == tag:
                    responses = tg["responses"]
                    print(random.choice(responses))
        else:
            print("I'm not sure I understood fully what you meant by that. Please ask me something else or is there "
                  "something else I could help you with?")


chat()