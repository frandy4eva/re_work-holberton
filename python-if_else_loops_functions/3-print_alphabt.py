#!/usr/bin/python3
"""Prints the ASCII alphabet, in lowercase without q and e"""
for alpha in range(ord('a'), ord('z') + 1):
    if alpha != ord('e') and alpha != ord('q'):
        print(chr(alpha), end='')
