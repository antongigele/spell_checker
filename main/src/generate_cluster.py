from difflib import get_close_matches
import pandas as pd
from sys import platform
from time import time
import json
import concurrent.futures

win_path = r"C:\Users\Anton\Desktop\projects\spell_checker\csv_imports\\"
mac_linux_path = "/Users/antongigele/Desktop/python/spell_checker/csv_imports/"

if platform == "linux" or platform == "linux2":
    path = mac_linux_path
elif platform == "darwin":
    path = mac_linux_path
elif platform == "win32":
    path = win_path
else:
    path = win_path

queries_df = pd.read_csv(path + "nlp_queries.csv")
queries_df = queries_df.drop(columns=["#"])
queries_df = queries_df.fillna("")

single_words_set = set()
for q in queries_df["query"].unique():
    single_words_set.update(set(q.split()))

def generate_clusters(word_atoms_set):
    atoms_clusters_dict = {}
    all_atoms_list = list(word_atoms_set)[:50]
    for atom in all_atoms_list:
        related_words_list = get_close_matches(atom, list(word_atoms_set), n=500, cutoff=0.85)
        atoms_clusters_dict[atom] = related_words_list
        word_atoms_set = word_atoms_set - set(related_words_list)
        # print(len(word_atoms_set))
    
    return atoms_clusters_dict

def multiprocess(function, dataset):
    # segments_list = [i for i in range(0, dataset_size+1, 10*1000)]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(function, dataset)

    all_results = {}
    for result in results:
        all_results.update(result)

    return all_results
if __name__ == "__main__":
    start = time()
    word_clusters = multiprocess(generate_clusters, single_words_set)
    stop = time()
    print(stop-start)
    with open("/Users/antongigele/Desktop/python/spell_checker/csv_imports/atom_clusters_small.json", "w") as outfile: 
        json.dump(word_clusters, outfile)