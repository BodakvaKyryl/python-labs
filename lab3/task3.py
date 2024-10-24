import nltk
import nltk.tokenize as tk
from nltk.stem import WordNetLemmatizer, PorterStemmer
import pymorphy3 as p3
from uk_stemmer import UkStemmer
import regex as re
import random as rnd
import string

path = "./text3.txt"
regex = r"[A-za-z\+\#]+"

with open(path, "r") as file:
    text = file.read()
    print("\n", text)
    languages = re.findall(regex, text)
    print("programming languages:", languages)
