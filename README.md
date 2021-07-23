# coding_example
coding example for AiTeR lab

* With anaconda, install tensorflow>=2.0 and proceed this task.
* Import additional modules required to implement the function.
* Use MNIST Data from tensorflow. (https://www.tensorflow.org/tutorials/quickstart/beginner?hl=ko)
* Use json module to import configuration.
* Use Sequence (tensorflow.keras.utils.Sequence) to construct dataloader.

# main.py
1. import configuration, network, dataloader, trainer.
2. Initialize class objects with configuration.
3. Write main function for train, evaluate and print.
	3-1. Use network class to obtain model object.
	3-2. Use trainer and dataloader classes to train model.
	3-3. Use trainer to evaluate the trained model.
	3-4. Write print_result function to print out "accuracy". (ex : 99.80%)
4. Evaluate model with test dataset.
5. print test result with print_result function.

# dataloader.py
1. Write Dataloader class.
	1-1. Write init function to obtain dataset.
	1-2. Write __len__ to obtain length of dataset.
	1-3. Write __getitem__ function to obtain batch from dataset.
	1-4. (optional) Write on_epoch_end to shuffle dataset indices or remove the function.
(https://minimin2.tistory.com/100)

# trainer.py
1. Write Trainer class.
	1-1. Write init function to obtain model and dataloader.
	1-2. Write compile function to compile model object.
		1-2-1. You may use callbacks (EarlyStopping, ModelCheckpoint, CSVLogger, TensorBoard, etcs)
		(refer tensorflow document : https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/EarlyStopping)
	1-3. Write train function to train model. (You may use 'fit' function from tensorflow.keras.Model)
	1-4. Write evaluate function to evaluate model. (You may use 'predict' function from tensorflow.keras.Model)

# network.py
1. Write Network class.
	1-1. Write init function to define your custom model.
	1-2. Write call function to define model foward pass.
(https://www.tensorflow.org/api_docs/python/tf/keras/Model)

# conf.json
1. Write configurations required for each experiment. (ex : batch_size, checkpoint path, layer dimensions)
(https://rfriend.tistory.com/474)
