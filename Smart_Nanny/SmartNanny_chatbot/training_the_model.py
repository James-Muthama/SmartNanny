from creating_model import model
from preprocessing_json_file import training
from preprocessing_json_file import output

# tries to load the model if it is not available we will need to train it
try:
    model.load("SmartNannyBot.tflearn")
except:
    # fitting the neural network with the training data, output, number of epochs, batch size and where it will show
    # metrics such as accuracy etc
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)

    # saving the model as SmartNannyBot.tflearn
    model.save("SmartNannyBot.tflearn")
