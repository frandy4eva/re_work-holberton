#!/usr/bin/python3
"""Prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase)"""
for alpha in range(ord('z'), ord('a') - 1, -1):
    alpha = chr(alpha)
    if ord(alpha) % 2 != 0:
        alpha = chr(ord(alpha) - 32)
    print(alpha, end='')
