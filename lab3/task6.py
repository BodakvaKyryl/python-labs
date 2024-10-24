import nltk
import nltk.tokenize as tk
from nltk.stem import WordNetLemmatizer, PorterStemmer
import pymorphy3 as p3
from uk_stemmer import UkStemmer
import regex as re
import random as rnd
import string

path = "./text6.txt"
regex_time = r"\d{2}:\d{2}:\d{2}"
regex_date = r"\d{4}-\d{2}-\d{2}"

with open(path, "r") as file:
    text = file.read()
    print("\n", text)
    dates = re.findall(regex_date, text)
    times = re.findall(regex_time, text)
    print("time:", times)
    print("dates:", dates)
    print("\nhours:", [time[0:2] for time in times])
    print("years:", [date[0:4] for date in dates])
