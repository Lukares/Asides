#!/bin/python3

import sys

def migratoryBirds(n, ar):
    dict = {}
    for bird in ar:
        if bird not in dict:
            dict[bird] = 1
        else:
            dict[bird] += 1
    return max(dict, key=dict.get)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
