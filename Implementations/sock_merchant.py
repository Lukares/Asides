#!/bin/python3

import sys

def sockMerchant(n, ar):
    dict = {}
    result = 0
    for val in ar:
        if val not in dict:
            dict[val] = 1
        else:
            dict[val] += 1
    values = list(dict.values())
    for x in values:
        result += (x // 2)
    return result

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
