import numpy as np
import random
from nltk.stem.lancaster import LancasterStemmer
from SmartNanny_chatbot.converting_input_to_numpy_array import bag_of_words
from SmartNanny_chatbot.training_the_model import model
from SmartNanny_chatbot.preprocessing_json_file import labels
from SmartNanny_chatbot.preprocessing_json_file import data
from SmartNanny_chatbot.preprocessing_json_file import words
from Whatsapp_Chatbot.reading_texts_from_whatsapp.reading_text_from_whatsapp import reading_text_from_whatsapp

stemmer = LancasterStemmer()


def chat():

    while True:
        text = reading_text_from_whatsapp()

        # takes in input from user passes it into the function bag_of_words
        results = model.predict([bag_of_words(text, words)])[0]

        # takes back the prediction with the highest probability
        results_index = np.argmax(results)

        # finds the tag with matching probability
        tag = labels[results_index]

        # only allows prediction with a 70% chance to be passed to the user any less passes an alternate response
        if results[results_index] > 0.7:
            for tg in data["intents"]:
                if tg["tag"] == tag:
                    responses = tg["responses"]

                    return random.choice(responses)
        else:
            return "I'm not sure I understood fully what you meant by that. Please ask me something else or is there " \
                   "something else I could help you with?"


chat()
