# import all the things here first 
import json
import numpy
import tensorflow 
import pickle
import random
import nltk


from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# now we have to load the intents.json file 
with open('intents.json') as file:
    data = json.load(file)

print(data)