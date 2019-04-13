#!/usr/bin/python

import os
import sys
import time
import string
import argparse
import itertools

#Define wordlist creater
def createWordList(chrs, min_length, max_length, output):
    """
    :param `chrs` is characters to iterate.
    :param `min_length` is minimum length of characters.
    :param `max_length` is maximum length of characters.
    :param `output` is output of wordlist file.
    """
    if min_length > max_length:
        print ("[!] Please `min_length` must smaller or same as with `max_length`")
        sys.exit()

    if os.path.exists(os.path.dirname(output)) == False:
        os.makedirs(os.path.dirname(output))

    print ('[+] Creating wordlist at `%s`...' % output)
    print ('[i] Starting time: %s' % time.strftime('%H:%M:%S'))

    output = open(output, 'w')

    for n in range(min_length, max_length + 1):
        for xs in itertools.product(chrs, repeat=n):
            chars = ''.join(xs)
            output.write("%s\n" % chars)
            sys.stdout.write('\r[+] saving character `%s`' % chars)
            sys.stdout.flush()
    output.close()

    print ('\n[i] End time: %s' % time.strftime('%H:%M:%S'))


if __name__ == '__main__':

    info = '''
        #######################################################################
        # Python WordList Generator  #  By JungleB00K
        #######################################################################
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        usages Example:
                Please Enter Here All Word for combination :  Avf$5.%
                please enter here lengh of words : 4
                please enetr here name of Wordlist :wordlist.txt
        **********************************************************************
        **********************************************************************
        '''
    print info
    print ""
    chrs=raw_input("[+] Please Enter Here All Word for combination : ")
    print ""
    print ""
    min_length=int(raw_input("[+] Please Enter Minimum Lenth Of Words  :   "))
    print ""
    max_length=int(raw_input("[+] Please Enter Maximum Lenth Of Words  :  "))
    print ""
    output= raw_input("[+] Please Enetr Here Name Of Wordlist File : ")

    createWordList(chrs, min_length, max_length, output)
