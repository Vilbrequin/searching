import unittest
import ctypes

# Load the shared library
search_lib = ctypes.CDLL('../functions/binary_search_iterative.o')

# Define the argument types and return type of the C function
search_lib.binary_search.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
search_lib.binary_search.restype = ctypes.c_int

class TestBinarySearchFunction(unittest.TestCase):
    def test_element_found(self):
        arr = (ctypes.c_int * 6)(12, 13, 24, 25, 36, 44)
        size = len(arr)
        element = 24
        result = search_lib.binary_search(arr, size, element)
        self.assertEqual(result, 2)
    
    def test_element_not_found_middle(self):
        arr = (ctypes.c_int * 6)(12, 13, 24, 25, 36, 44)
        size = len(arr)
        element = 27
        result = search_lib.binary_search(arr, size, element)
        self.assertEqual(result, -1)

    def test_element_not_found_start(self):
        arr = (ctypes.c_int * 6)(12, 13, 24, 25, 36, 44)
        size = len(arr)
        element = 10
        result = search_lib.binary_search(arr, size, element)
        self.assertEqual(result, -1)
    
    def test_element_not_found_end(self):
        arr = (ctypes.c_int * 6)(12, 13, 24, 25, 36, 44)
        size = len(arr)
        element = 50
        result = search_lib.binary_search(arr, size, element)
        self.assertEqual(result, -1)

    def test_element_at_start(self):
        arr = (ctypes.c_int * 6)(12, 13, 24, 25, 36, 44)
        size = len(arr)
        element = 12
        result = search_lib.binary_search(arr, size, element)
        self.assertEqual(result, 0)

    def test_element_at_end(self):
        arr = (ctypes.c_int * 6)(12, 13, 24, 25, 36, 44)
        size = len(arr)
        element = 44
        result = search_lib.binary_search(arr, size, element)
        self.assertEqual(result, 5)
    
    def test_element_at_middle(self):
        arr = (ctypes.c_int * 6)(12, 13, 24, 25, 36, 44)
        size = len(arr)
        element = 25
        result = search_lib.binary_search(arr, size, element)
        self.assertEqual(result, 3)
    
    def test_single_element_array(self):
        arr = (ctypes.c_int * 1)(12)
        size = len(arr)
        element = 12
        result = search_lib.binary_search(arr, size, element)
        self.assertEqual(result, 0)
        element = 13
        result = search_lib.binary_search(arr, size, element)
        self.assertEqual(result, -1)
    
    def test_empty_array(self):
        arr = (ctypes.c_int * 0)()
        size = len(arr)
        element = 1
        result = search_lib.binary_search(arr, size, element)
        self.assertEqual(result, -1)

    def test_even_number_array(self):
        arr = (ctypes.c_int * 6)(12, 13, 24, 25, 36, 44)
        size = len(arr)
        element = 36
        result = search_lib.binary_search(arr, size, element)
        self.assertEqual(result, 4)

    def test_odd_number_array(self):
        arr = (ctypes.c_int * 7)(12, 13, 24, 25, 36, 44, 55)
        size = len(arr)
        element = 13
        result = search_lib.binary_search(arr, size, element)
        self.assertEqual(result, 1)
    
    def test_duplicate_elements(self):
        arr = (ctypes.c_int * 7)(12, 13, 24, 25, 44, 44, 55)
        size = len(arr)
        element = 44
        result = search_lib.binary_search(arr, size, element)
        self.assertIn(result, [4, 5])
    

    


if __name__ == "__main__" :
    unittest.main()