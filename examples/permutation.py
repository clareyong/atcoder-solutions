from pprint import pprint

def r_permutation(s, depth):
    if len(s) == 1:
        return [[s[0]]]
    permutations = []
    for i in range(len(s)):
        c = s[i]
        the_rest = s[:i] + s[i+1:]
        permutations_of_the_rest = r_permutation(the_rest, depth+1)
        for permutation_of_the_rest in permutations_of_the_rest:
            permutation_of_the_rest.append(c)
            permutations.append(permutation_of_the_rest)
    return permutations


def permutation(s):
    r = r_permutation(s, 0)
    return [''.join(item) for item in r]


if __name__ == "__main__":
    pprint(permutation('abc'))
