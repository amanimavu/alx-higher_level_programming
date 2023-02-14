import unittest
"""
module: test_rectangle - used to test the rectangle module
"""
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    setUp method of the TestRectangle class is called
    every time a TestCase is encountered to make sure
    all necessary resources required to execute the
    TestCases are available
    """
    def setUp(self):
        print("Set up")
        self.rect_1 = Rectangle(10, 22)
        self.w1 = 37
        self.x1 = 4
        self.y1 = 11
        self.rect_2 = Rectangle(21, 11, id=5)
        self.h1 = 30
        self.rect_3 = Rectangle(15, 12, 8, 4, 7)
        self.x2 = 1
        self.y2 = 9
        self.rect_4 = Rectangle(3, 3)

    """
    test_width TestCase is used to test wheteher the
    correct width size is returned
    """
    def test_width(self):
        self.assertEqual(self.rect_1.width, 10)
        self.assertEqual(self.rect_2.width, 21)

    """
    test_set_width is used to test if the width
    attribute of the rectangle is correctly set.
    It also test validation of the width property
    """
    def test_set_width(self):
        self.rect_1.width = self.w1
        self.assertTrue(self.rect_1.width == 37)
        with self.assertRaises(TypeError):
            self.rect_1.width = "21"
        with self.assertRaises(ValueError):
            self.rect_1.width = 0

    """
    test_id_allocation is used to test whether the
    correct id is returned
    """
    def test_id_allocation(self):
        self.assertEqual(self.rect_2.id, 5)
        self.assertEqual(self.rect_3.id, 7)

    """
    The test_id_allocation_no_id tests if the correct id
    is returned when a Rectangle object is instanciated
    with no id and if the TestCase isn't the very first
    one. This is because the setUp method is called every
    time a TestCase runs
    """
    @unittest.expectedFailure
    def test_id_allocation_no_id(self):
        self.assertEqual(self.rect_1.id, 1)

    """
    test_height tests whether the correct size of the
    height is returned
    """
    def test_height(self):
        self.assertEqual(self.rect_1.height, 22)
        self.assertEqual(self.rect_2.height, 11)

    """
    test_set_height test validates the width that is
    to be set and checks whether the heighth property
    is correctly set
    """
    def test_set_height(self):
        self.rect_2.height = self.h1
        self.assertEqual(self.rect_2.height, 30)
        with self.assertRaises(TypeError):
            self.rect_1.height = "10"
        with self.assertRaises(ValueError):
            self.rect_2.height = -2

    """
    test_x test whether the correct x coordinate
    postion is returned
    """
    def test_x(self):
        self.assertEqual(self.rect_1.x, 0)
        self.assertEqual(self.rect_3.x, 8)

    """
    test_set_x validates the x coordinate position that
    is to be set and checks whether the width is
    correctly set
    """
    def test_set_x(self):
        self.rect_1.x = self.x1
        self.assertEqual(self.rect_1.x, 4)
        self.rect_3.x = self.x2
        self.assertEqual(self.rect_3.x, 1)
        with self.assertRaises(TypeError):
            self.rect_1.x = "12"
        with self.assertRaises(ValueError):
            self.rect_3.x = -4

    """
    test_y checks whether the correct y coordinate
    position
    """
    def test_y(self):
        self.assertEqual(self.rect_1.y, 0)
        self.assertEqual(self.rect_3.y, 4)

    """
    test_set_y validates the y coordinate position
    and checks whether the y coordinate postion is
    correctly set
    """
    def test_set_y(self):
        self.rect_1.y = self.y1
        self.rect_3.y = self.y2
        self.assertEqual(self.rect_1.y, 11)
        self.assertEqual(self.rect_3.y, 9)
        with self.assertRaises(TypeError):
            self.rect_1.y = "22"
        with self.assertRaises(ValueError):
            self.rect_3.y = -7

    """
    test_area checks whether the correct area of
    the Rectangle object was computed
    """
    def test_area(self):
        self.assertEqual(self.rect_1.area(), 220)

    """
    test_str checks whether the correct string
    is returned from __str__ magic method
    """
    def test_str(self):
        self.assertEqual(str(self.rect_2), "[Rectangle] (5) 0/0 - 21/11")


"""
use the unittest module to run the test file
only if the test file is executed from the
terminal and not executed as module
"""
if __name__ == "__main__":
    unittest.main()
