from nltk import edit_distance
from nltk import word_tokenize, sent_tokenize
import nltk
import pandas as pd

# sentence = "yuo call"

word_list = [
    "work",
    "call",
    "man",
    "woman",
    "use",
    "way",
    "have",
    "try",
    "person",
    "day",
    "time",
    "get",
    "look",
    "point",
    "make",
    "yo"
    ]

def get_closest_sentence(query_string):

    tokenized_sentence = word_tokenize(query_string)

    closest_terms = {}
    for term in tokenized_sentence:

        distance_dict = {}
        for word in word_list:
            distance_dict[word] = edit_distance(term, word)
        closest_terms[term] = distance_dict

    print(min(closest_terms[tokenized_sentence[0]], key=closest_terms[tokenized_sentence[0]].get), min(closest_terms[tokenized_sentence[1]], key=closest_terms[tokenized_sentence[1]].get))

queries_df = pd.read_csv("../csv_imports/nlp_queries.csv")
