import unittest
import ctypes
import numpy as np

# Load the shared library
search_lib = ctypes.CDLL('functions/interpolation_search_function.o')

# Define the argument types and return type of the C function
search_lib.interpolation_search.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
search_lib.interpolation_search.restype = ctypes.c_int

class TestInterpolationSearchFunction(unittest.TestCase):
    def test_element_found(self):
        arr = (ctypes.c_int * 5)(1, 2, 3, 4, 5)
        size = len(arr)
        element = 3
        result = search_lib.interpolation_search(arr, size, element)
        self.assertEqual(result, 2)

    def test_element_not_found(self):
        arr = (ctypes.c_int * 5)(1, 2, 3, 4, 5)
        size = len(arr)
        element = 6
        result = search_lib.interpolation_search(arr, size, element)
        self.assertEqual(result, -1)

    def test_empty_array(self):
        arr = (ctypes.c_int * 0)()
        size = len(arr)
        element = 1
        result = search_lib.interpolation_search(arr, size, element)
        self.assertEqual(result, -1)

    def test_single_element_array(self):
        arr = (ctypes.c_int * 1)(5)
        size = len(arr)
        element = 4
        result = search_lib.interpolation_search(arr, size, element)
        self.assertEqual(result, -1)

    def test_large_array(self):
        arr = np.arange(1, 1001, dtype=np.int32)
        arr_c = (ctypes.c_int * len(arr))(*arr)
        size = len(arr)
        element = 750
        result = search_lib.interpolation_search(arr_c, size, element)
        self.assertEqual(result, 749)

    def test_element_at_start(self):
        arr = (ctypes.c_int * 5)(1, 2, 3, 4, 5)
        size = len(arr)
        element = 1
        result = search_lib.interpolation_search(arr, size, element)
        self.assertEqual(result, 0)

    def test_element_at_end(self):
        arr = (ctypes.c_int * 5)(1, 2, 3, 4, 5)
        size = len(arr)
        element = 5
        result = search_lib.interpolation_search(arr, size, element)
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        arr = (ctypes.c_int * 5)(-5, -4, -3, -2, -1)
        size = len(arr)
        element = -3
        result = search_lib.interpolation_search(arr, size, element)
        self.assertEqual(result, 2)

    def test_large_numbers(self):
        arr = (ctypes.c_int * 5)(100000, 200000, 300000, 400000, 500000)
        size = len(arr)
        element = 300000
        result = search_lib.interpolation_search(arr, size, element)
        self.assertEqual(result, 2)

    def test_mixed_numbers(self):
        arr = (ctypes.c_int * 5)(-10, -5, 0, 5, 10)
        size = len(arr)
        element = 5
        result = search_lib.interpolation_search(arr, size, element)
        self.assertEqual(result, 3)

    def test_duplicate_elements(self):
        arr = (ctypes.c_int * 8)(1, 2, 2, 2, 3, 4, 4, 5)
        size = len(arr)
        element = 2
        result = search_lib.interpolation_search(arr, size, element)
        self.assertIn(result, [1, 2, 3])  # Can be any of the duplicate positions

    def test_array_with_zeros(self):
        arr = (ctypes.c_int * 5)(0, 0, 0, 0, 0)
        size = len(arr)
        element = 0
        result = search_lib.interpolation_search(arr, size, element)
        self.assertIn(result, [0, 1, 2, 3, 4])  # Can be any position since all are zeros

    def test_element_not_found_in_large_array(self):
        arr = np.arange(1, 10001, dtype=np.int32)
        arr_c = (ctypes.c_int * len(arr))(*arr)
        size = len(arr)
        element = 10001
        result = search_lib.interpolation_search(arr_c, size, element)
        self.assertEqual(result, -1)

    def test_element_found_in_large_array(self):
        arr = np.arange(1, 10001, dtype=np.int32)
        arr_c = (ctypes.c_int * len(arr))(*arr)
        size = len(arr)
        element = 7500
        result = search_lib.interpolation_search(arr_c, size, element)
        self.assertEqual(result, 7499)

if __name__ == '__main__':
    unittest.main()
