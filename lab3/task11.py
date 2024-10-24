import nltk
import nltk.tokenize as tk
from nltk.stem import WordNetLemmatizer, PorterStemmer
import pymorphy3 as p3
from uk_stemmer import UkStemmer
import regex as re
import random as rnd
import string

path = "./text11.txt"
stop_words_path = "./stopWordsUa.txt"

with open(path, "r", encoding="utf-8") as file, open(
    stop_words_path, "r", encoding="utf-8"
) as stop_words_file:
    text = file.read().lower()
    print("\n", text)

    stop_words = stop_words_file.read().lower().split("\n")
    print("\nstop words:", stop_words)

    words = tk.word_tokenize(text)
    print("\nwords:", words)

    filtered_words = [
        word
        for word in words
        if word not in string.punctuation and word not in stop_words
    ]
    print("\nfiltered words:", filtered_words)

    print("\nstatistics:")
    print("words count:", len(words))

    punctuation_list = [word for word in words if word in string.punctuation]

    print("punctuation count:", len(punctuation_list))
    print("stop words count:", len(words) - len(filtered_words) - len(punctuation_list))
    print("filtered words count:", len(filtered_words))

    lem = p3.MorphAnalyzer(lang="uk")
    lem_words = [lem.parse(word)[0].normal_form for word in filtered_words]
    print("\nLemmed words:", lem_words)

    stem = UkStemmer()
    stem_words = [stem.stem_word(word) for word in filtered_words]
    print("\nStemmed words:", stem_words)
