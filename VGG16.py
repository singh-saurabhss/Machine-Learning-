import pandas as pd
import numpy as np
import cv2
from tqdm import tqdm
import os
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import VGG16
from random import shuffle
from keras.layers import Conv2D,MaxPool2D,Dense,Dropout,Activation,Flatten
from keras.models import Sequential
from keras.optimizers import Adam
from keras.models import Model
from keras.models import load_model



IMG_SIZE = 128

img_dir = r'C:\Users\asus\Downloads\Compressed\flowers'     ### enter your image directory
c=0
list_of_dir = []
Total_flower_data = []

for dir_in in os.listdir(img_dir):
    list_of_dir.append(dir_in)
for i in tqdm(range(len(list_of_dir))):
    for img in (os.listdir(os.path.join(img_dir,list_of_dir[i]))):    
        path = os.path.join((os.path.join(img_dir,list_of_dir[i])),img)
        #print(os.path.join(img_dir,list_of_dir[i]))
        img = cv2.imread(path)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE)) 
        Total_flower_data.append([np.array(img),np.array(list_of_dir[i])]) 
        shuffle(Total_flower_data)
        
        
data = pd.DataFrame(Total_flower_data,columns=['flower','label'])

my_new_model = Sequential()
my_new_model.add(VGG16(include_top=False,
                       pooling='avg',
                       weights='imagenet'))
my_new_model.add(Dense(5,activation='softmax'))

my_new_model.layers[0].trainable = False

my_new_model.compile(optimizer='sgd',
                     loss='categorical_crossentropy',
                     metrics=['accuracy'])


datagen = ImageDataGenerator(rescale=1./255,
                             width_shift_range=0.1,
                             height_shift_range=0.1,
                             rotation_range=90,
                             horizontal_flip=True)


val_gen = datagen.flow_from_directory('Compressed/val_data',
        target_size=(IMG_SIZE,IMG_SIZE),
        batch_size=20,
        class_mode='categorical')

train_gen = datagen.flow_from_directory(
        'Compressed/Flowers',
        target_size=(IMG_SIZE,IMG_SIZE),
        batch_size=10,
        class_mode='categorical')

my_new_model.fit_generator(train_gen,              
                    steps_per_epoch=500,
                    epochs=20,
                    validation_data=val_gen,
                    validation_steps=400)

test_dir = r'C:\Users\asus\Downloads\Compressed\flower_test_images'
test_flower_data = []    
for img in tqdm(os.listdir(test_dir)):
    path_test = os.path.join(test_dir,img)
    img_num_id = img.split('.')[0]
    img = cv2.imread(path_test)
    img = cv2.resize(img,(IMG_SIZE,IMG_SIZE))
    test_flower_data.append([np.array(img),img_num_id])

y1 = (np.array([i for i in data['label']]))
from sklearn.preprocessing import LabelEncoder
lab = LabelEncoder()
#y = lab.fit_transform(y)
y1 = lab.fit_transform(y1)
lab.classes_



array = np.unique(y1)
flower_name = np.unique(data['label'])
print(flower_name)
import matplotlib.pyplot as plt
        
label_dict={}
for i in range(len(array)):
    label_dict[i] = flower_name[i]

count = 0
for num,data in enumerate(test_flower_data):
    img_data = data[0]
    plt.subplot(3,6,num+1)
    orig = img_data
    reshaped_data = img_data.reshape(-1,IMG_SIZE,IMG_SIZE,3)
    prediction = my_new_model.predict([reshaped_data])[0]
    if np.argmax(prediction) == 0: word_label = label_dict.get(np.argmax(prediction))
    if np.argmax(prediction) == 1: word_label = label_dict.get(np.argmax(prediction))
    if np.argmax(prediction) == 2: word_label = label_dict.get(np.argmax(prediction))
    if np.argmax(prediction) == 3: word_label = label_dict.get(np.argmax(prediction))
    if np.argmax(prediction) == 4: word_label = label_dict.get(np.argmax(prediction))
    plt.axis("off")
    plt.imshow(cv2.cvtColor(orig, cv2.COLOR_BGR2RGB))
    plt.title(word_label)
plt.show()
