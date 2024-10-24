import nltk
import nltk.tokenize as tk
from nltk.stem import WordNetLemmatizer, PorterStemmer
import pymorphy3 as p3
from uk_stemmer import UkStemmer
import regex as re
import random as rnd
import string

path = "./text1.txt"
vowels = "aeiou"

with open(path, "r") as file:
    text = file.read()
    print("\n", text)

    words = [word for word in tk.word_tokenize(text) if re.match(r"\w+", word)]
    print("\nnumber of words:", len(words))

    vowels_starts = [word for word in words if word.lower()[0] in vowels]
    print(
        "\nwords, that starts with vowel:",
        vowels_starts,
        "\namount:",
        len(vowels_starts),
    )

    three_words = [words[rnd.randint(0, len(words) - 1)] for _ in range(3)]
    print("\nthree words:", three_words)

    old_word = words[rnd.randint(0, len(words) - 1)]
    new_word = "Bodakva"
    text = re.sub(r"\b" + old_word + r"\b", new_word, text)
    print(
        "\nthat chosen one word:",
        old_word,
        "\nnew word:",
        new_word,
        "\nchanged text:",
        text,
    )
