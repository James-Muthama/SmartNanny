from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

from preprocessing_json_file import training
from preprocessing_json_file import output
import tflearn
import tensorflow

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
