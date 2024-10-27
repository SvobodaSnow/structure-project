import re

dictionary_path = {}
dictionary_function = {}
dictionary_reg_function = {}
dictionary_reg_path = {}


def load_dictionary_function():
    for s in open('library/dictionary_function.txt', encoding="utf-8").readlines():
        s = s[:-1].split(";")
        dictionary_function[s[0].upper()] = ";".join(s[1:])
    return


def load_dictionary_path():
    for s in open('library/dictionary_path.txt', encoding="utf-8").readlines():
        s = s[:-1].split(";")
        dictionary_path[s[0].upper()] = ";".join(s[1:])
    return


def load_dictionary_reg_function():
    for s in open('library/dictionary_reg_function.txt', encoding="utf-8").readlines():
        s = s[:-1].split(";")
        dictionary_reg_function[s[0]] = ";".join(s[1:])
    return


def load_dictionary_reg_path():
    for s in open('library/dictionary_reg_path.txt', encoding="utf-8").readlines():
        s = s[:-1].split(";")
        dictionary_reg_path[s[0]] = ";".join(s[1:])
    return


def get_description_path(name_path: str):
    return dictionary_path[name_path] if name_path in dictionary_path else search_reg_path_description(name_path)


def get_description_function(name_function: str):
    return dictionary_function[
        name_function] if name_function in dictionary_function else search_reg_function_description(name_function)


def search_reg_function_description(name_function):
    for sr in dictionary_reg_function:
        answer = re.search(sr, name_function)
        if answer:
            a = re.search(r'\d{1,}', name_function)
            return dictionary_reg_function[sr].format(a[0] if a else "")
    return name_function


def search_reg_path_description(name_path):
    for sr in dictionary_reg_path:
        answer = re.search(sr, name_path)
        if answer:
            a = re.search(r'\d{1,}', name_path)
            return dictionary_reg_path[sr].format(a[0] if a else "")
    return name_path


def unload_file_dictionary_function(file_name: str):
    open(file_name, "w", encoding="utf-8").writelines(
        open('library/dictionary_function.txt', encoding="utf-8").readlines())
    return


def unload_file_dictionary_path(file_name: str):
    open(file_name, "w", encoding="utf-8").writelines(
        open('library/dictionary_path.txt', encoding="utf-8").readlines())
    return


def unload_file_dictionary_reg_function(file_name: str):
    open(file_name, "w", encoding="utf-8").writelines(
        open('library/dictionary_reg_function.txt', encoding="utf-8").readlines())
    return


def unload_file_dictionary_reg_path(file_name: str):
    open(file_name, "w", encoding="utf-8").writelines(
        open('library/dictionary_reg_path.txt', encoding="utf-8").readlines())
    return


def load_file_dictionary_function(file_name: str):
    open('library/dictionary_function.txt', 'w', encoding="utf-8").writelines(
        open(file_name, encoding="utf-8").readlines())
    return


def load_file_dictionary_path(file_name: str):
    open('library/dictionary_path.txt', 'w', encoding="utf-8").writelines(
        open(file_name, encoding="utf-8").readlines())
    return


def load_file_dictionary_reg_function(file_name: str):
    open('library/dictionary_reg_function.txt', 'w', encoding="utf-8").writelines(
        open(file_name, encoding="utf-8").readlines())
    return


def load_file_dictionary_reg_path(file_name: str):
    open('library/dictionary_reg_path.txt', 'w', encoding="utf-8").writelines(
        open(file_name, encoding="utf-8").readlines())
    return


def load_from_def_file_dictionary_function():
    open('library/dictionary_function.txt', 'w', encoding="utf-8").writelines(
        open('library/default_dictionary/dictionary_function.txt', encoding="utf-8").readlines())
    return


def load_from_def_file_dictionary_path():
    open('library/dictionary_path.txt', 'w', encoding="utf-8").writelines(
        open('library/default_dictionary/dictionary_path.txt', encoding="utf-8").readlines())
    return


def load_from_def_file_dictionary_reg_function():
    open('library/dictionary_reg_function.txt', 'w', encoding="utf-8").writelines(
        open('library/default_dictionary/dictionary_reg_function.txt', encoding="utf-8").readlines())
    return


def load_from_def_file_dictionary_reg_path():
    open('library/dictionary_reg_path.txt', 'w', encoding="utf-8").writelines(
        open('library/default_dictionary/dictionary_reg_path.txt', encoding="utf-8").readlines())
    return


def load_to_def_file_dictionary_function():
    open('library/default_dictionary/dictionary_function.txt', 'w', encoding="utf-8").writelines(
        open('library/dictionary_function.txt', encoding="utf-8").readlines())
    return


def load_to_def_file_dictionary_path():
    open('library/default_dictionary/dictionary_path.txt', 'w', encoding="utf-8").writelines(
        open('library/dictionary_path.txt', encoding="utf-8").readlines())
    return


def load_to_def_file_dictionary_reg_function():
    open('library/default_dictionary/dictionary_reg_function.txt', 'w', encoding="utf-8").writelines(
        open('library/dictionary_reg_function.txt', encoding="utf-8").readlines())
    return


def load_to_def_file_dictionary_reg_path():
    open('library/default_dictionary/dictionary_reg_path.txt', 'w', encoding="utf-8").writelines(
        open('library/dictionary_reg_path.txt', encoding="utf-8").readlines())
    return


load_dictionary_function()
load_dictionary_path()
load_dictionary_reg_path()
load_dictionary_reg_function()
