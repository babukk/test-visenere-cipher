#! /usr/bin/env python3

import os
import sys
import getopt

x_table = [chr(i) for i in range(127)]
x_table_len = len(x_table)

encode = lambda c, k: (c + k ) % x_table_len
decode = lambda c, k: (c - k + x_table_len) % x_table_len
z_list = lambda val: zip(range(0, len(val)), val)


def doCipher(v, k, func):
    """doCipher - returns encrypted/decrypted string

    Arguments:
    v -- source string
    k -- key string
    func -- function ref.
    """
    k_len = len(k)
    v = z_list(v)
    e = [func(ord(c), ord(k[i % k_len])) for (i, c) in v]
    return '' . join([ x_table[c] for c in e ])


def main():
    my_key = None
    mode = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hedk:", ["help", "encode", "decode", "key",])

    except getopt.GetoptError as err:
        print("Unhandled option: " + str(err))
        return 1

    for opt_name, opt_val in opts:
        if opt_name in ("-h", "--help"):
            print("usage: python visenere.py -e|--encode | -d|--decode -k|--key")
            sys.exit(0)
        elif opt_name in ("-e", "--encode"):
            mode = 'encode'
        elif opt_name in ("-d", "--decode"):
            mode = 'decode'
        elif opt_name in ("-k", "--key"):
            my_key = opt_val

    if my_key is None:
        print("Key undefined.")
        return 1

    if mode == 'encode':
        data = sys.stdin.readlines()
        data = ''.join(data).replace("\n", "")
        print(doCipher(data, my_key, encode))
        return 0
    elif mode == 'decode':
        data = sys.stdin.readlines()
        data = ''.join(data).replace("\n", "")
        print(doCipher(data, my_key, decode))
        return 0
    else:
        print("Undefined or wrong mode.")
        return 1

    return 0


if   __name__ == "__main__":
    sys.exit(main())
