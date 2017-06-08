def find_permutations(user_str):
    permutations  = ["cake", "caek", "ckea", "ckae", "ceka", "ceak", "akec", "akce", "acke", "acek", "aeck", "aekc", "keca", "keac", "kace", "kaec", "kcea", "kcae", "ekac", "ekca", "eack", "eakc", "ecka"]
    print(user_str)
    print(user_str[0])
    # loop over string
    # start with keeping i same and shifting other parts over - change i
    # user_str[0] + user_str[1] - user_str[n]
    # re- run with shifted user string- shift first letter to last?
    # if not in permutations - add to list
    print(permutations.sort())
    return permutations


find_permutations("aaa")

find_permutations("cake")

find_permutations("banana")

