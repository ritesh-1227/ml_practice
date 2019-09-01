from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

clf = Sequential()
clf.add(Convolution2D(32,3,3,input_shape = (64,64,3),activation = 'relu'))
clf.add(MaxPooling2D(pool_size = (2,2)))
clf.add(Flatten())
clf.add(Dense(output_dim = 128,activation = 'relu'))
clf.add(Dense(output_dim = 1,activation = 'sigmoid'))

clf.compile(optimizer = 'adam',loss = 'binary_crossentropy')

from keras.preprocessing.image import ImageDatagenerator

fig = ImageDataGenerator(rescale = 1.0/255)
testfig = ImageDataGenerator(rescale = 1.0/255)

traind = fig.flow_from_directory(r'',target_size = (64,64),batch_size = 32,class_mode = 'binary')
testd = testfig.flow_from_directory(r'',target_size = (64,64),batch_size = 32,class_mode = 'binary')

clf.fit_generator(traind,samples_per_epoch = 50, nb_epoch = 10, validation_data = testd, nb_val_samples = 1000)

clf.save('clf_model.hdf5')
