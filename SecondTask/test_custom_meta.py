import unittest

from custom_meta import CustomMeta


class TestClass(metaclass=CustomMeta):

    field = 2

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value


class TestCustomMeta(unittest.TestCase):

    def test_classic_attributes(self):
        tc = TestClass(1)
        self.assertRaises(AttributeError, lambda: tc.get_value())
        self.assertRaises(AttributeError, lambda: tc.set_value(2))
        self.assertRaises(AttributeError, lambda: tc.field)

    def test_custom_attributes(self):
        tc = TestClass(2)
        self.assertEqual(tc.custom_get_value(), 2)
        tc.custom_set_value(3)
        self.assertEqual(tc.custom_field, 2)
