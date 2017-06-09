class Permutations:

    def find_permutations(self, user_str):
        """Return all possible permutations of given string"""
        permutations = []
        print(user_str)
        print(user_str[0])
        # loop over string
        # start with keeping i same and shifting other parts over - change i
        # user_str[0] + user_str[1] - user_str[n]
        # re- run with shifted user string- shift first letter to last?
        # if not in permutations - add to list
        permutations.sort()
        print(permutations)
        return permutations
