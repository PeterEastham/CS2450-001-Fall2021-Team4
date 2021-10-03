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

        zero_dict = {
            "asdf" : "0",
            "fdsa" : "0",
            "5gts" : "0",
        }

        one_dict = {
            "foobar" : "1",
            "fooooooooobbbbaaaaarrrr" : "1",
            "afoobar" : "1",
        }

        two_dict = {
            "barfoo" : "2",
            "aassfd" : "2",
            "fooabar" : "2"
        }

        single_a = sub_dict_from_keys(test_dict, "a")
        multi_a = sub_dict_from_keys(test_dict, "aaaaaaaaaaaaaaaa")

        foo = sub_dict_from_keys(test_dict, "foo")
        fo = sub_dict_from_keys(test_dict, "fo")

        foo_bar = sub_dict_from_keys(test_dict, "foobar")
        perm_foo_bar = sub_dict_from_keys(test_dict, "foooooobbbbbbarrrrr")

        value_zero = sub_dict_from_values(test_dict, "0")
        value_one = sub_dict_from_values(test_dict, "1")
        value_two = sub_dict_from_values(test_dict, "2")


        self.assertDictEqual(first_dict, single_a)
        self.assertDictEqual(first_dict, multi_a)

        self.assertDictEqual(second_dict, foo)
        self.assertDictEqual(second_dict, fo)

        self.assertDictEqual(third_dict, foo_bar)
        self.assertDictEqual(third_dict, perm_foo_bar)

        self.assertDictEqual(value_zero, zero_dict)
        self.assertDictEqual(value_one, one_dict)
        self.assertDictEqual(value_two, two_dict)

        #Test that the Dictionary Filter Wrapper Works as Expected

        single_a = sub_emp_id_dict(test_dict, "a")
        multi_a = sub_emp_id_dict(test_dict, "aaaaaaaaaaaaaaaa")

        foo = sub_emp_id_dict(test_dict, "foo")
        fo = sub_emp_id_dict(test_dict, "fo")

        foo_bar = sub_emp_id_dict(test_dict, "foobar")
        perm_foo_bar = sub_emp_id_dict(test_dict, "foooooobbbbbbarrrrr")

        value_zero = sub_emp_id_dict(test_dict, "0")
        value_one = sub_emp_id_dict(test_dict, "1")
        value_two = sub_emp_id_dict(test_dict, "2")

        bad_input = sub_emp_id_dict(test_dict, "-")
        empty_input = sub_emp_id_dict(test_dict, "")

        self.assertDictEqual(first_dict, single_a)
        self.assertDictEqual(first_dict, multi_a)

        self.assertDictEqual(second_dict, foo)
        self.assertDictEqual(second_dict, fo)

        self.assertDictEqual(third_dict, foo_bar)
        self.assertDictEqual(third_dict, perm_foo_bar)

        self.assertDictEqual(value_zero, zero_dict)
        self.assertDictEqual(value_one, one_dict)
        self.assertDictEqual(value_two, two_dict)

        self.assertDictEqual(bad_input, test_dict)
        self.assertDictEqual(empty_input, test_dict)
