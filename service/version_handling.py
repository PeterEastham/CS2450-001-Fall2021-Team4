from model import *


#Gets all the Properties of a Class, Coverts it to a CSV, and returns that string.
def get_class_properties_string(object):
    properties = ""
    for property in object.__dict__.keys():
        properties += property
        properties += ","

    return properties[:-1] + "\n"
