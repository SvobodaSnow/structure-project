import re


dictionary_path = {}
dictionary_function = {}
dictionary_reg = {}

f = open('library/dictionary_function.txt', encoding="utf-8").readlines()
for s in f:
    s = s[:-1].split(";")
    dictionary_function[s[0].upper()] = ";".join(s[1:])

f = open('library/dictionary_path.txt', encoding="utf-8").readlines()
for s in f:
    s = s[:-1].split(";")
    dictionary_path[s[0].upper()] = ";".join(s[1:])

f = open('library/dictionary_reg.txt', encoding="utf-8").readlines()
for s in f:
    s = s[:-1].split(";")
    dictionary_reg[s[0]] = ";".join(s[1:])

def get_description_path(name_path: str):
    return dictionary_path[name_path] if name_path in dictionary_path else name_path

def get_description_function(name_function: str):
    return dictionary_function[name_function] if name_function in dictionary_function else search_reg_description(name_function)

def search_reg_description(name_function):
    answer = None
    for sr in dictionary_reg:
        answer = re.search(sr, name_function)
        if answer:
            a = re.search(r'\d{1,}', name_function)
            return dictionary_reg[sr].format(a[0] if a else "")
    return name_function
