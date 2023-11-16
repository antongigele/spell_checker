from nltk import edit_distance
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, words
import nltk
import pandas as pd

print(words)

# sentence = "yuo call it a lax"

# queries_df = pd.read_csv("C:\Users\Anton\Desktop\projects\spell_checker\csv_imports\nlp_queries.csv")

path = "C:\Users\Anton\Desktop\projects\spell_checker\csv_imports\nlp_queries.csv"

def load_and_preprocess_words(path):
    queries_df = pd.read_csv(path)
    
    return queries_df.drop_duplicates(subset="query")["query"]



word_list = [
    "work",
    "call",
    "cali",
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

    result_list = [min(closest_terms[tokenized_sentence[i]], key=closest_terms[tokenized_sentence[i]].get) for i in range(len(tokenized_sentence))]

    return result_list
    # return min(closest_terms[tokenized_sentence[0]], key=closest_terms[tokenized_sentence[0]].get), min(closest_terms[tokenized_sentence[1]], key=closest_terms[tokenized_sentence[1]].get))

# print(get_closest_sentence(sentence))
