import unittest
import coverage
from majestic import majestic_etl, top_list

coverage.exclude('if __name__ == "__main__":')

class MajesticTest(unittest.TestCase):

    def test_etl(self):
        a = majestic_etl()
        first = next(a)

        # first should have a rank of 1 and the second part should be a domain
        self.assertEqual(first[0], 1,
                         f"First item in majestic_etl did not have a rank of 1, it had a rank of {first[0]}")

        # simple check to see that the first result is a domain
        # i.e. has a dot in it
        self.assertTrue('.' in first[1],
                        "majestic_etl did not return a URL")

    def test_top_list(self):
        a = top_list(10)
        self.assertEqual(len(a), 10, "top_list did not return 10 items")
        self.assertEqual(a[0][0], 1, "first item was not ranked #1")
        self.assertEqual(a[9][0], 10, f"tenth item was not ranked #10, rank of {a[9][0]} provided")

if __name__ == "__main__":
    unittest.main()
