#!/usr/bin/env python3
# HW08_ch11_ex01
# Write a function that reads the words in words.txt and stores them as keys
# in a dictionary (returning the dictionary). It doesn’t matter what the
# values are. Then you can use the in operator as a fast way to check whether
# a string is in the dictionary.
###############################################################################
# Imports


# Body
def store_to_dict(filename):
    with open(filename,'r') as f:
        d={}
        n=0
        txt=f.read()
        names=txt.split()
        for name in names:
            d[name] = n
            n+=1
    return d


###############################################################################
def main():  # DO NOT CHANGE BELOW
    words_dict = store_to_dict('words.txt')
    if "this" in words_dict:
        print("Yup.")
    if "qwertyuiop" in words_dict:
        print("Hmm.")

if __name__ == '__main__':
    main()
