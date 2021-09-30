import re

def sub_dict_from_keys(dictionary, search_string):
    subset = _remaker(search_string)
    return {k:v for (k, v) in dictionary.items() if subset.search(k) != None}

def sub_dict_from_values(dictionary, search_string):
    subset = _remaker(search_string)
    return {k:v for (k, v) in dictionary.items() if subset.search(v) != None}

def _remaker(search_string):

    re_string = "+".join(_reduce_string(search_string))
    re_string += "+"
    return re.compile(re_string)

def _reduce_string(original_string):
    answer_string = ""
    for letter in original_string:
        if not answer_string.endswith(letter):
            answer_string += letter
    return answer_string
