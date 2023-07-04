import nltk

from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow
import pickle
import random
import json

# opening the intents.json file
with open("intents.json", encoding="utf8") as file:
    data = json.load(file)

# this try and except allow us to avoid preprocessing the data in the .json if it is already saved
try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)

except:
    # creating arrays to stor values from the intents.json file
    words = []
    labels = []
    docs_x = []
    docs_y = []

    # loops through the .json file
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            # uses the nltk.word_tokenize() to get the syllables of the words in pattern
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)

            # stores the tokenized words and tags under docs_x and docs_y respectively
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        # stores the tags from the .json file
        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    # converts the words list to lowercase letters and arranges them alphabetically
    words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
    words = sorted(list(set(words)))

    # sorts the list of tags alphabetically
    labels = sorted(labels)

    # create empty training and output lists
    training = []
    output = []

    # create a list that has zeros for every tag available i.e [0,0,0,0]
    out_empty = [0 for _ in range(len(labels))]

    # loop through doc_x which contains the all the patterns from the .json file, with enumerate x will store the
    # index we are on in the list while doc will store the particular pattern we are on in the list
    for x, doc in enumerate(docs_x):
        # create an empty list for the bag of words
        bag = []

        # store the individual words from the patterns as a lowercase letter
        wrds = [stemmer.stem(w.lower()) for w in doc]

        # compare a word in wrds from above to the list of tokenized words in the lists word and store 1 into the list
        # bag if comparison is found else 0
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        # copy the out_empty list into output_row
        output_row = out_empty[:]

        # checks for the specific tag in docs_y that is matched to the pattern in x and returns its index in the labels
        # lists and converts that index in the output_row that was full of zero's to a one
        output_row[labels.index(docs_y[x])] = 1

        # append the bag of words into the empty training list
        training.append(bag)
        # append the output_row into the empty output list
        output.append(output_row)

    # convert training and output into numpy arrays
    training = np.array(training)
    output = np.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

# resets the tensorflow graph to get rid of previous settings
tensorflow.compat.v1.reset_default_graph()

# tflearn.input_data() specifics the input data of the model
net = tflearn.input_data(shape=[None, len(training[0])])
# creates a dense neural network with 8 neurons
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
# creates an output layer with neurons equal to the number of tags, also uses a softmax as the activation function
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

# creating the Dense Neural Network and equates it to model
model = tflearn.DNN(net)

# tries to load the model if it is not available we will need to train it
try:
    model.load("SmartNannyBot.tflearn")
except:
    # fitting the neural network with the training data, output, number of epochs, batch size and where it will show
    # metrics such as accuracy etc
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)

    # saving the model as SmartNannyBot.tflearn
    model.save("SmartNannyBot.tflearn")


# create a function that takes in input from a user converts it into a numpy array to feed into the model
def bag_of_words(s, words):
    # creates the bag of words
    bag = [0 for _ in range(len(words))]

    # tokenizes every word inputted by the user and stems them
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    # fills the bag of words with 1 if a stemmed word matches a word from the words list
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    # returns a numpy array to be passed in the model
    return np.array(bag)


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
