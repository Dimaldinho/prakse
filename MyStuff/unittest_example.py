# test_list_concatenator.py
import unittest
from list_concatenator import concatenate_lists

class TestListConcatenator(unittest.TestCase):

    def test_concatenate_lists(self):
        # Known results for 10 data points
        known_results = [
            ([1], [2], [1, 2]),
            ([], [3, 4], [3, 4]),
            ([1, 2, 3], [], [1, 2, 3]),
            ([1, 2], [3, 4], [1, 2, 3, 4]),
            ([1, 2], [], [1, 2]),
            ([], [1, 2], [1, 2]),
            ([1, 2, 3, 4, 5], [6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
            ([9, 8, 7], [6, 5], [9, 8, 7, 6, 5]),
            ([], [], []),
            ([1, 2, 3], [1, 2, 3], [1, 2, 3, 1, 2, 3])
        ]

        # Generate test cases for 100 data points based on known results
        for i in range(10):
            for input1, input2, expected_output in known_results:
                result = concatenate_lists(input1 * i, input2 * i)
                self.assertEqual(result, expected_output * i)

if __name__ == '__main__':
    unittest.main()