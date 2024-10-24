import nltk
import nltk.tokenize as tk
from nltk.stem import WordNetLemmatizer, PorterStemmer
import pymorphy3 as p3
from uk_stemmer import UkStemmer
import regex as re
import random as rnd
import string

path = "./text8.txt"
stop_words_path = "./stopWords.txt"

with open(path, "r") as file, open(stop_words_path, "r") as stop_words_file:
    text = file.read().lower()
    print("\n", text)

    stop_words = stop_words_file.read().lower().split("\n")
    print("\nstop words:", stop_words)

    sentences = tk.sent_tokenize(text)
    words = tk.word_tokenize(text)
    print("\nsentences:", sentences)
    print("\nwords:", words)

    filtered_words = [
        word
        for word in words
        if word not in string.punctuation and word not in stop_words
    ]
    print("\nfiltered words:", filtered_words)

    tagged_words = nltk.pos_tag(filtered_words)
    print("\nwords and their types:", tagged_words)

    print("\nTASK 9:")
    print(
        "words count per sentence (№, count):",
        [(i + 1, len(sentences[i])) for i in range(0, len(sentences))],
    )
    print(
        "stop words count for all text:",
        len([word for word in words if word in stop_words]),
    )

    longest_word = max(words, key=len)
    print("longest word:", longest_word, "; lenght:", len(longest_word))

    words_with_lenght_4 = [word for word in words if len(word) == 4]
    print(
        "amount of words of 4 symbol lenght:",
        len(words_with_lenght_4),
        "; words:",
        words_with_lenght_4,
    )

    print("\nTASK10")
    lem = WordNetLemmatizer()
    lem_words = [lem.lemmatize(word) for word in filtered_words]
    print("\nLemmed words:", lem_words)

    stem = PorterStemmer()
    stem_words = [stem.stem(word) for word in filtered_words]
    print("\nStemmed words:", stem_words)
