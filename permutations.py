my_string = input("please enter a string: ")

class Permutations:

    def find_permutations(self, my_string):
        """Return all possible permutations of given string"""
        if len(my_string)<=1:
            return [my_string]

        perms = self.find_permutations(my_string[1:])
        char = my_string[0]
        variations = []
        for perm in perms:
            # insert the character into every possible location
            for i in range(len(perm) + 1):
                variations.append(perm[:i] + char + perm[i:])

        variations.sort()
        print(variations)
        return variations

Permutations().find_permutations(my_string)
