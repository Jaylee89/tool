#!/usr/bin/python3
""" A simple utility to validate ID for Chinese

    References:
    o https://jingyan.baidu.com/article/ff4116259e0a7112e48237b9.html
    o https://www.cnblogs.com/xudong-bupt/p/3293838.html
"""

import sys

def get_verification_code(id17):
    l_wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    l_vc = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    s = 0
    for i in range(len(l_wi)):
        s += l_wi[i] * int(id17[i])
    m = s % 11
    return l_vc[m]


def is_valid_id(cn_id):
    cn_id_17 = cn_id[0:-1]
    vc = get_verification_code(cn_id_17)
    if vc != cn_id[-1]:
        return False
    return True


def main():
    with open('dates.txt', 'r') as file:
        dates_array = [line.strip() for line in file.readlines()]
    final_result = ""

    for cn_id in dates_array:
        result = is_valid_id(cn_id)
        final_result = final_result + f"{cn_id}, {result}\n"

    with open('dates-results.txt', 'w') as file:
        file.write(final_result)

if __name__ == '__main__':
    sys.exit(main())