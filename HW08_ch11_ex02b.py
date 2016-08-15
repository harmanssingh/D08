#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports


# Body
def print_hist_old(h):
    for c in h:
        print(c, h[c])

def print_hist_new(h):
    list1=[]
    for c in h:
        list1.append(c)
    list1.sort()
    for keys in list1:
        print(keys,h[keys])



###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def histogram_old(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def histogram_new(s):
    d = dict()
    for c in s:
        d[c]=d.get(c,0)
        d[c]+=1
    return d


def get_pledge_list():
    with open('pledge.txt','r') as f:
        wordlist=f.read()
        words=wordlist.split()
        return words

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the
    histogram of pledge.txt.
    """
    print_hist_new(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()
