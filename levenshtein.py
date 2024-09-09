'''
Dhruti Vadlamudi
Spell Checker Project
'''

import Levenshtein


def levenshtein_distance(x, y):
    n = len(x)
    m = len(y)
    A = [[i + j for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n):
        for j in range(m):
            A[i + 1][j + 1] = min(A[i][j + 1] + 1,
                                  A[i + 1][j] + 1,
                                  A[i][j] + int(x[i] != y[j]))
    return A[n][m]


def lev_distance(s1, s2):
    return Levenshtein.distance(s1, s2)
