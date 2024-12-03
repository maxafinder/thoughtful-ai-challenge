import unittest
from robotic_arm import PackageType, validate_inputs, is_heavy, is_bulky, sort


class TestValidateInputs(unittest.TestCase):
    def test_valid_inputs(self):
        try:
            validate_inputs(10, 10, 10, 10)
        except ValueError:
            self.fail("validate_inputs raised ValueError unexpectedly")

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            validate_inputs(-10, 10, 10, 10)
        with self.assertRaises(ValueError):
            validate_inputs(10, -10, 10, 10)
        with self.assertRaises(ValueError):
            validate_inputs(10, 10, -10, 10)
        with self.assertRaises(ValueError):
            validate_inputs(10, 10, 10, -10)
        with self.assertRaises(ValueError):
            validate_inputs("10", 10, 10, 10)


class TestIsHeavy(unittest.TestCase):
    def test_is_heavy(self):
        self.assertTrue(is_heavy(20))

    def test_is_not_heavy(self):
        self.assertFalse(is_heavy(10))


class TestIsBulky(unittest.TestCase):
    def test_is_bulky(self):
        self.assertTrue(is_bulky(120, 100, 100))
        self.assertTrue(is_bulky(150, 100, 50))

    def test_is_not_bulky(self):
        self.assertFalse(is_bulky(50, 50, 50))


class TestSort(unittest.TestCase):
    def test_standard_package(self):
        self.assertEqual(sort(10, 10, 10, 10), PackageType.STANDARD)

    def test_special_package(self):
        self.assertEqual(sort(120, 100, 100, 10), PackageType.SPECIAL)
        self.assertEqual(sort(10, 10, 10, 20), PackageType.SPECIAL)

    def test_rejected_package(self):
        self.assertEqual(sort(120, 100, 100, 20), PackageType.REJECTED)

if __name__ == '__main__':
    unittest.main()
