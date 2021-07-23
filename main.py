'''
Main for process all.
'''
import json
from nerwork import Network
from dataloader import Dataloader
from trainer import Trainer
# define main function
def main:
    # load configuration
    with open('conf.json','r') as fid:
        conf = json.load(fid)

    # load and normalize dataset
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    # initialize each class objects
    model = Network('''arguments''')
    trainer = Trainer('''arguments''')
    dataloader = Dataloader('''arguments''')
    
    # train model
    trainer.train('''arguments''')

    # evaluate model
    prediction = trainer.evaluate('''arguments''')

    # print accuracy of model
    print_result(prediction, y_test)
    
# define function to print result
def print_result(prediction, y_test):
    '''write detailed functions'''
    
if __name__ == '__main__':
    main()