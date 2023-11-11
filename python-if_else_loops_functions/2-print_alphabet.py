#!/usr/bin/python3
"""Prints the ASCII alphabet, in lowercase"""
for alpha in range(ord('a'), ord('z') + 1):
    print(chr(alpha), end='')
