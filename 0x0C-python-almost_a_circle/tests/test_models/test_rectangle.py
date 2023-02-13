import unittest
"""
module: test_rectangle - used to test the rectangle module
"""
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    This class tests the getter and setter methods of
    the class Rectangle
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

    def test_width(self):
        self.assertEqual(self.rect_1.width, 10)
        self.assertEqual(self.rect_2.width, 21)

    def test_set_width(self):
        self.rect_1.width = self.w1
        self.assertTrue(self.rect_1.width == 37)
        with self.assertRaises(TypeError):
            self.rect_1.width = "21"
        with self.assertRaises(ValueError):
            self.rect_1.width = 0

    def test_id_allocation(self):
        self.assertEqual(self.rect_2.id, 5)
        self.assertEqual(self.rect_3.id, 7)

    @unittest.expectedFailure
    def test_id_allocation_no_id(self):
        self.assertEqual(self.rect_1.id, 1)

    def test_height(self):
        self.assertEqual(self.rect_1.height, 22)
        self.assertEqual(self.rect_2.height, 11)

    def test_set_height(self):
        self.rect_2.height = self.h1
        self.assertEqual(self.rect_2.height, 30)
        with self.assertRaises(TypeError):
            self.rect_1.height = "10"
        with self.assertRaises(ValueError):
            self.rect_2.height = -2

    def test_x(self):
        self.assertEqual(self.rect_1.x, 0)
        self.assertEqual(self.rect_3.x, 8)

    def test_set_x(self):
        self.rect_1.x = self.x1
        self.assertEqual(self.rect_1.x, 4)
        self.rect_3.x = self.x2
        self.assertEqual(self.rect_3.x, 1)
        with self.assertRaises(TypeError):
            self.rect_1.x = "12"
        with self.assertRaises(ValueError):
            self.rect_3.x = -4

    def test_y(self):
        self.assertEqual(self.rect_1.y, 0)
        self.assertEqual(self.rect_3.y, 4)

    def test_set_y(self):
        self.rect_1.y = self.y1
        self.rect_3.y = self.y2
        self.assertEqual(self.rect_1.y, 11)
        self.assertEqual(self.rect_3.y, 9)
        with self.assertRaises(TypeError):
            self.rect_1.y = "22"
        with self.assertRaises(ValueError):
            self.rect_3.y = -7

    def test_area(self):
        self.assertEqual(self.rect_1.area(), 220)

    def test_str(self):
        self.assertEqual(str(self.rect_2), "[Rectangle] (5) 0/0 - 21/11")

if __name__ == "__main__":
    unittest.main()
