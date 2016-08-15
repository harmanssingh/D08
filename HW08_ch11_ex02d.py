#!/usr/bin/env python3
# HW08_ch11_ex02d.py
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Update print_hist_new from HW08_ch11_ex02b.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
###############################################################################
# Imports


# Body
def invert_dict_old(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse[val] = inverse.get(val,[])
        inverse[val].append(key)
    return inverse


def print_hist_newest(d):
    print_hist_new(d)

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def print_hist_old(h):
    for c in h:
        print(c, h[c])


def print_hist_new(h):
    list1=[]
    for c in h:
        list1.append(c)
    list1.sort()
    for keys in list1:
        print('{} : {}'.format(repr(keys),repr(h[keys])))



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



def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()
