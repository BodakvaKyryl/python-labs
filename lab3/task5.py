import nltk
import nltk.tokenize as tk
from nltk.stem import WordNetLemmatizer, PorterStemmer
import pymorphy3 as p3
from uk_stemmer import UkStemmer
import regex as re
import random as rnd
import string

path = "./text5.txt"
regex = r"5{2,3}"

with open(path, "r") as file:
    text = file.read()
    print("\n", text)
    numbers = [number for number in text.split(" ") if re.search(regex, number)]
    print("numbers with 2-3 fives in them:", numbers)
