import unittest

from service.list_reducer import *
from service.version_handling import *

"""
We don't test the file_helper since it's used so much in other tests, that if it
isn't behaving as expected, we'll catch it that way.
"""
class ServiceModuleTest(unittest.TestCase):

    def test_list_reducer(self):
        test_dict = {
            "asdf" : "0",
            "foobar" : "1",
            "barfoo" : "2",
            "fdsa" : "0",
            "fooooooooobbbbaaaaarrrr" : "1",
            "aassfd" : "2",
            "5gts" : "0",
            "afoobar" : "1",
            "fooabar" : "2"
        }
        #Should include all keys with an 'a' in them
        first_dict = {
            "asdf" : "0",
            "foobar" : "1",
            "barfoo" : "2",
            "fdsa" : "0",
            "fooooooooobbbbaaaaarrrr" : "1",
            "aassfd" : "2",
            "afoobar" : "1",
            "fooabar" : "2"
        }
        #All 'foo' strings
        second_dict = {
            "foobar" : "1",
            "barfoo" : "2",
            "fooooooooobbbbaaaaarrrr" : "1",
            "afoobar" : "1",
            "fooabar" : "2"
        }
        #All 'foobar' strings
        third_dict = {
            "foobar" : "1",
            "fooooooooobbbbaaaaarrrr" : "1",
            "afoobar" : "1",
        }

        single_a = sub_dict_from_keys(test_dict, "a")
        multi_a = sub_dict_from_keys(test_dict, "aaaaaaaaaaaaaaaa")

        foo = sub_dict_from_keys(test_dict, "foo")
        fo = sub_dict_from_keys(test_dict, "fo")

        foo_bar = sub_dict_from_keys(test_dict, "foobar")
        perm_foo_bar = sub_dict_from_keys(test_dict, "foooooobbbbbbarrrrr")


        self.assertDictEqual(first_dict, single_a)
        self.assertDictEqual(first_dict, multi_a)

        self.assertDictEqual(second_dict, foo)
        self.assertDictEqual(second_dict, fo)

        self.assertDictEqual(third_dict, foo_bar)
        self.assertDictEqual(third_dict, perm_foo_bar)
