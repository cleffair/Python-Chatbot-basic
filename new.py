# import all the things here first 
import json
import numpy
import tensorflow as tf
import pickle as pk
import random
import nltk

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer

#loading our intentsjson file now 

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = [] 
ignoreLetters = ['!', '?', '.', ',']


for intent in intents['intents']:
    for pattern in intent['patterns']:
        wordList = nltk.word_tokenize(pattern)
        words.extend(wordList)
        documents.append((wordlist, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])