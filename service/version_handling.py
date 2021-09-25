from model import *


#Gets all the Properties of a Class, Coverts it to a CSV, and returns that string.
def class_csv_headers(object):
    properties = ""
    for property in object.__dict__.keys():
        properties += property
        properties += ","

    return properties[:-1] + "\n"


"""
Employee mapper Option

header_to_version = {
    "header_str" : "emp_1",
    "other_header" : "emp_1_1"
    ----------etc-------------
}
"""
