import tflearn
import tensorflow
from nltk.stem.lancaster import LancasterStemmer
from Smart_Nanny.SmartNanny_chatbot import training
from Smart_Nanny.SmartNanny_chatbot import output

stemmer = LancasterStemmer()

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
