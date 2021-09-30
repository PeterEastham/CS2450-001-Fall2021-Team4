import re

def sub_dict_from_keys(dictionary, search_string):
    subset = _remaker(search_string)
    return {k:v for (k, v) in dictionary.items() if subset.match(k)}

def sub_dict_from_values(dictionary, search_string):
    subset = _remaker(search_string)
    return {k:v for (k, v) in dictionary.items() if subset.match(v)}

def _remaker(search_string):
    re_string = "+".join(search_string)
    re_string += "+"
    return re.compile(re_string)
