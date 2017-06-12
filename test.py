import unittest
from permutations import Permutations


class TestPermutations(unittest.TestCase, Permutations):

    def setUp(self):
        self.find_permutations = Permutations.find_permutations(self, my_string)

    def test_permutations(self):
        self.assertEqual(Permutations.find_permutations(self, my_string="be"), ["be", "eb"])
        self.assertEqual(Permutations.find_permutations(self, my_string="aaa"), ["aaa"])
        self.assertEqual(Permutations.find_permutations(self, my_string="cake"), ["acek", "acke", "aeck", "aekc", "akce", "akec",
                                                                        "caek", "cake", "ceak", "ceka", "ckae", "ckea",
                                                                        "eack", "eakc", "ecka", "ekac", "ekca", "ecka"])
        self.assertEqual(Permutations.find_permutations(self,  my_string="banana"), ["aaannb", "aabana", "ananab", "annaba", "annbaa", "annaab",
                                                                          "baaann", "baanna", "banaan", "banana", "bnanaa", "bnnaaa",
                                                                          "naaabn", "naaban", "nanaab", "nanaba", "nanbaa", "nbnaaa"]
)


if __name__ == '__main__':
    unittest.main()




