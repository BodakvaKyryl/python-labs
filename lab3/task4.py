import nltk
import nltk.tokenize as tk
from nltk.stem import WordNetLemmatizer, PorterStemmer
import pymorphy3 as p3
from uk_stemmer import UkStemmer
import regex as re
import random as rnd
import string

path = "./text4.txt"
regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

with open(path, "r") as file:
    text = file.read()
    print("\n", text)
    emails = re.findall(regex, text)
    print("all emails:", emails)
