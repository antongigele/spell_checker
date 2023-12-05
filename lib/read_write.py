import json
import csv

### read
with open('/Users/antongigele/Desktop/python/spell_checker/csv_imports/porn_acronyms.json') as json_file:
    acronyms_dict = json.load(json_file)

### write
with open("/Users/antongigele/Desktop/python/spell_checker/csv_imports/atoms.csv", "w", newline="") as outfile: 
    write = csv.writer(outfile)
    write.writerow(list())

with open("/Users/antongigele/Desktop/python/spell_checker/csv_imports/porn_acronyms.json", "w") as outfile: 
        json.dump(source, outfile)