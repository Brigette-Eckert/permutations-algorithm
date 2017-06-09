import unittest
from permutations import Permutations


class TestPermutations(unittest.TestCase):

    def test_permutations(self):
        self.assertEqual(Permutations.find_permutations(self, "be"), ["be", "eb"])
        self.assertEqual(Permutations.find_permutations(self, "aaa"), ["aaa"])
        self.assertEqual(Permutations.find_permutations(self, "cake"), ["acek", "acke", "aeck", "aekc", "akce", "akec",
                                                                        "caek", "cake", "ceak", "ceka", "ckae", "ckea",
                                                                        "eack", "eakc", "ecka", "ekac", "ekca", "ecka"])
        self.assertEqual(Permutations.find_permutations(self, "banana"), ["aaannb", "aabana", "ananab", "annaba", "annbaa", "annaab",
                                                                          "baaann", "baanna", "banaan", "banana", "bnanaa", "bnnaaa",
                                                                          "naaabn", "naaban", "nanaab", "nanaba", "nanbaa", "nbnaaa"]
)


if __name__ == '__main__':
    unittest.main()




