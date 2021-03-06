import unittest

from custom_list import CustomList


class TestCustomList(unittest.TestCase):

    def test_add(self):
        # test result value
        cl1 = CustomList([1, 2, 3])
        cl2 = CustomList([2, 3])
        self.assertEqual(cl1 + cl2, CustomList([3, 5, 3]), "add1")
        self.assertEqual(cl2 + cl1, CustomList([3, 5, 3]), "add2")

        cl1 = CustomList()
        cl2 = CustomList([1, 2, 3])
        self.assertEqual(cl1 + cl2, CustomList([1, 2, 3]), "add3")
        self.assertEqual(cl2 + cl1, CustomList([1, 2, 3]), "add4")

        # test result type
        lst = [-5, 1]
        self.assertIsInstance(cl2 + lst, CustomList, "add5")
        self.assertIsInstance(lst + cl2, CustomList, "add6")

        self.assertEqual(cl2 + lst, [-4, 3, 3], "add7")
        self.assertEqual(lst + cl2, [-4, 3, 3], "add8")

    def test_sub(self):

        cl1 = CustomList()
        cl2 = CustomList([1, 2, 3, 4])
        self.assertEqual(cl1 - cl2, CustomList([-1, -2, -3, -4]), "sub1")
        self.assertEqual(cl2 - cl1, CustomList([1, 2, 3, 4]), "sub2")

        cl1 = CustomList([1, 2, 3, 4])
        cl2 = CustomList([4, 5, -7])
        self.assertEqual(cl1 - cl2, CustomList([-3, -3, 10, 4]), "sub3")
        self.assertEqual(cl2 - cl1, CustomList([3, 3, -10, -4]), "sub4")

        lst = [-2, 1]
        self.assertIsInstance(cl1 - lst, CustomList, "sub5")
        self.assertIsInstance(lst - cl1, CustomList, "sub6")

        self.assertEqual(cl1 - lst, CustomList([3, 1, 3, 4]), "sub7")
        self.assertEqual(lst - cl1, CustomList([-3, -1, -3, -4]), "sub8")

    def test_comp(self):
        # equal
        cl1 = CustomList([1, 2, 3])
        cl2 = CustomList([1, 2, 3])
        self.assertEqual(cl1, cl2, "comp1")
        self.assertLessEqual(cl1, cl2, "comp2")
        self.assertGreaterEqual(cl1, cl2, "comp3")

        cl1 = CustomList([1, 2, 3, 4, -4])
        cl2 = CustomList([1, 2, 3, 6, -6])
        self.assertEqual(cl1, cl2, "comp4")
        self.assertLessEqual(cl1, cl2, "comp5")
        self.assertGreaterEqual(cl1, cl2, "comp6")

        # less
        cl1 = CustomList([-5, -3, -2])
        cl2 = CustomList([1])

        self.assertLess(cl1, cl2, "comp7")
        self.assertLessEqual(cl1, cl2, "comp8")
        self.assertNotEqual(cl1, cl2, "comp9")

        # greater
        self.assertGreater(cl2, cl1, "comp10")
        self.assertGreaterEqual(cl2, cl1, "comp11")
        self.assertNotEqual(cl2, cl1, "comp12")


if __name__ == "__main__":
    unittest.main()
