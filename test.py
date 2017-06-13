import unittest
from permutations import Permutations


class TestPermutations(unittest.TestCase, Permutations):

    def setUp(self):
        my_string = "cake"
        self.find_permutations = Permutations.find_permutations(self, my_string)

    def test_permutations(self):
        self.assertEqual(Permutations().find_permutations("be"), ["be", "eb"])
        self.assertEqual(Permutations().find_permutations("aaa"), ["aaa"])
        self.assertEqual(Permutations().find_permutations("cake"), ["acek", "acke", "aeck", "aekc", "akce", "akec",
                                                                        "caek", "cake", "ceak", "ceka", "ckae", "ckea",
                                                                        "eack", "eakc", "ecka", "ekac", "ekca", "ecka"])
        self.assertEqual(Permutations().find_permutations("banana"), ["aaannb", "aabana", "ananab", "annaba", "annbaa", "annaab",
                                                                          "baaann", "baanna", "banaan", "banana", "bnanaa", "bnnaaa",
                                                                          "naaabn", "naaban", "nanaab", "nanaba", "nanbaa", "nbnaaa"]
)


if __name__ == '__main__':
    unittest.main()




# find a way to set my_string to kwarg[1]
#error list object is not callable