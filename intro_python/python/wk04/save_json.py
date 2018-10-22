import json
a = {'a':1,'c':2,'d':3}

with open('animal-questions.json', 'w') as data_file:
    json.dump(a, data_file, indent = 4, sort_keys = True)
