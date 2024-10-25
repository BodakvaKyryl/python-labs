import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import gutenberg, stopwords
import string
import math
import matplotlib.pyplot as plt


def calculate_tf(lemmas: list[str]) -> dict[str, float]:
    lemmas_count = len(lemmas)
    tf_values = {
        lemma: round(lemmas.count(lemma) / lemmas_count, 3) for lemma in set(lemmas)
    }
    print("TF values:", tf_values)
    return tf_values


def filter_unique(lemmas: list[str]) -> list[str]:
    unique_lemmas = list(set(lemmas))
    print("Unique lemmas:", unique_lemmas, "\nTotal:", len(unique_lemmas))
    return unique_lemmas


def process_text(file_path: str, stop_words_file: str) -> list[str]:
    with open(file_path, "r") as text_file, open(stop_words_file, "r") as stop_file:
        text_content = text_file.read().lower()
        stop_words = set(stop_file.read().lower().split())
        words = [
            word
            for word in word_tokenize(text_content)
            if word not in string.punctuation and word not in stop_words
        ]
        lemmatizer = WordNetLemmatizer()
        lemmas = [lemmatizer.lemmatize(word) for word in words]

        print("Filtered and lemmatized words:", lemmas, "\nCount:", len(lemmas))
        return lemmas


text_files = [
    "./4_sentences.txt",
    "./4_sentences_1.txt",
    "./4_sentences_2.txt",
    "./4_sentences_3.txt",
]

stop_words_file = "./stopWords.txt"

main_lemmas = process_text(text_files[0], stop_words_file)
main_unique_lemmas = filter_unique(main_lemmas)
tf_main = calculate_tf(main_lemmas)

other_docs_lemmas = [
    filter_unique(process_text(file, stop_words_file)) for file in text_files[1:]
]
other_docs_lemmas.append(main_unique_lemmas)

# Task 3: Calculating IDF
idf_values = {}
total_docs = len(other_docs_lemmas)

for lemma in tf_main:
    docs_with_lemma = sum(1 for doc in other_docs_lemmas if lemma in doc)
    idf_values[lemma] = round(math.log10(total_docs / docs_with_lemma), 3)

print("IDF values:", idf_values)

# Task 4: Calculating TF-IDF
tf_idf = {
    lemma: round(tf_main[lemma] * idf_values[lemma], 3) for lemma in sorted(tf_main)
}
print("TF-IDF values:", tf_idf)

# Task 5: Visualization
plt.figure(figsize=(10, 5))
plt.bar(tf_idf.keys(), tf_idf.values(), color="purple")
plt.title("TF-IDF Word Importance Evaluation", fontsize=14)
plt.xlabel("Words", fontsize=12)
plt.ylabel("TF-IDF", fontsize=12)
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.3)
plt.show()

# Task 6-7: Analyzing "Hamlet" text
# nltk.download("gutenberg")
# nltk.download("stopwords")

hamlet_words = gutenberg.words("shakespeare-hamlet.txt")
hamlet_filtered = [
    word.lower()
    for word in hamlet_words
    if word.lower() not in stopwords.words("english") and word not in string.punctuation
]

lemmatizer = WordNetLemmatizer()
hamlet_lemmas = [lemmatizer.lemmatize(word) for word in hamlet_filtered]

# Display text information
print("Total words in Hamlet:", len(hamlet_lemmas))
print("Sample of first 25 lemmas:", hamlet_lemmas[:25])

unique_hamlet_lemmas = list(set(hamlet_lemmas))
print("Unique lemmas count:", len(unique_hamlet_lemmas))
print("Sample of unique lemmas:", unique_hamlet_lemmas[:25])

# Special words analysis
special_characters = ["hamlet", "horatio", "ghost", "polonius"]
tf_special = {
    word: round(hamlet_lemmas.count(word) / len(hamlet_lemmas), 5)
    for word in special_characters
}
print("TF for special characters:", tf_special)

nltk.Text(hamlet_lemmas).dispersion_plot(special_characters)

# Task 7: Hapaxes and word length frequency
hapaxes = nltk.FreqDist(hamlet_lemmas).hapaxes()
print("Hapaxes count:", len(hapaxes))
print("Sample of hapaxes:", hapaxes[:25])

word_lengths = [len(word) for word in hamlet_filtered]
length_freq = {length: word_lengths.count(length) for length in set(word_lengths)}
common_length = max(length_freq, key=length_freq.get)
print("Most frequent word length:", common_length)

# Plotting word length frequency
fdist_lengths = nltk.FreqDist(word_lengths)
lengths_data = {str(length): fdist_lengths[length] for length in sorted(fdist_lengths)}

plt.figure(figsize=(10, 5))
plt.bar(lengths_data.keys(), lengths_data.values(), color="blue")
plt.ylim(2, 4000)
plt.xlabel("Word Length", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.title("Word Length Distribution in Hamlet", fontsize=14)
plt.savefig("./word_length_distribution.png")
plt.show()
