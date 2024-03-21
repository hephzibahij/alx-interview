#!/usr/bin/python3

def minOperations(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return 1 + minOperations(n-1)
    return minOperations(n//2)
