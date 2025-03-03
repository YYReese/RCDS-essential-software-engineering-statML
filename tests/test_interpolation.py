import unittest

def linear_interpolation(x1, y1, x2, y2, x):
    if x1 == x2:
        raise ValueError("x1 and x2 must be different")
    if x < x1 or x > x2:
        raise ValueError("x is outside the range of x1 and x2")
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)

class TestLinearInterpolation(unittest.TestCase):

    def test_linear_interpolation_basic(self):
        """Test basic interpolation between two points"""
        self.assertEqual(linear_interpolation(0, 0, 2, 2, 1), 1.0)
    
    def test_linear_interpolation_negative_values(self):
        """Test interpolation with negative values"""
        self.assertEqual(linear_interpolation(-1, -2, 1, 2, 0), 0.0)
    
    def test_linear_interpolation_decimal_points(self):
        """Test interpolation with decimal points"""
        self.assertAlmostEqual(linear_interpolation(0.5, 1.5, 2.5, 3.5, 1.5), 2.5)

    def test_linear_interpolation_horizontal_line(self):
        """Test interpolation along horizontal line (same y-values)"""
        self.assertEqual(linear_interpolation(1, 5, 3, 5, 2), 5.0)

    def test_linear_interpolation_vertical_line(self):
        """Test that vertical line raises ValueError"""
        with self.assertRaises(ValueError) as excinfo:
            linear_interpolation(2, 1, 2, 5, 2)
        self.assertIn("x1 and x2 must be different", str(excinfo.exception))

    def test_linear_interpolation_out_of_range(self):
        """Test that out-of-range x values raise ValueError"""
        with self.assertRaises(ValueError) as excinfo:
            linear_interpolation(1, 1, 3, 3, 4)
        self.assertIn("outside the range", str(excinfo.exception))

    def test_linear_interpolation_endpoints(self):
        """Test interpolation at endpoints"""
        x1, y1 = 0, 1
        x2, y2 = 2, 3
        self.assertEqual(linear_interpolation(x1, y1, x2, y2, x1), y1)
        self.assertEqual(linear_interpolation(x1, y1, x2, y2, x2), y2)

if __name__ == '__main__':
    unittest.main()