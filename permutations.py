
class Permutations:

    def find_permutations(self, user_str):
        """Return all possible permutations of given string"""
        if len(user_str)<=1:
            return [user_str]

        perms = self.find_permutations(user_str[1:])
        char = user_str[0]
        variations = []
        for perm in perms:
            # insert the character into every possible location
            for i in range(len(perm) + 1):
                variations.append(perm[:i] + char + perm[i:])

        variations.sort()
        print(variations)
        return variations

