#!/usr/bin/python3
"""Prints all possible different combinations of two digits"""
for num in range(10):
    for sub_num in range(num + 1, 10):
        if num != sub_num:
            if num == 8 and sub_num == 9:
                print(f"{num}{sub_num}", end='\n')
            else:
                print(f"{num}{sub_num}", end=', ')
