import pandas as pd
import numpy as np
from collections import OrderedDict
from ordered_set import OrderedSet

def create_single_words_list(dataframe):
    single_words_set = OrderedSet()
    for q in dataframe["query"].unique():
        single_words_set.update(set(q.split()))
    return list(single_words_set)

# def create_single_words_list(dataframe, list_len=0):
#     single_words_dict = OrderedDict()

#     queries_list = list(dataframe["query"].unique())
#     for q in queries_list:
#         for word in q.split():
#             single_words_dict[word] = None  # Using the keys of OrderedDict for uniqueness
    
#     single_words_list = list(single_words_dict.keys())
    
#     return single_words_list

if __name__ == "__main__":
    queries_df = pd.read_csv("/Users/antongigele/Desktop/python/spell_checker/csv_imports/nlp_queries.csv")
    queries_df = queries_df.drop(columns=["#"])
    queries_df = queries_df.fillna("")
    print(len(create_single_words_list(queries_df)))