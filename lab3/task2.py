import nltk
import nltk.tokenize as tk
from nltk.stem import WordNetLemmatizer, PorterStemmer
import pymorphy3 as p3
from uk_stemmer import UkStemmer
import regex as re
import random as rnd
import string

path = "./text2.txt"

with open(path, "r", encoding="utf-8") as file:
    text = file.read()
    print("\n", text)
    words = [word for word in tk.word_tokenize(text) if re.match(r"\w+", word)]
    letters = [letter for word in words for letter in word]
    print("\nall letters:", letters, "\ncount:", len(letters))

    print(
        "\nfirst 2 letter of each word:",
        [word[0 : min(2, len(words))] for word in words],
    )

    with_exluded_letters = [letter for letter in letters if letter not in ("a", "b")]
    print(
        "\nlist of letters without 'a' and 'b':",
        with_exluded_letters,
        "\ncount:",
        len(with_exluded_letters),
    )
