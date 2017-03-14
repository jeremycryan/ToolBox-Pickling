""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load
import codecs


def update_counter(file_name, reset=False):
    if not reset and exists(file_name):
        file1 = open(file_name, 'rb')
        counter = load(file1) + 1
        file1.close()
        file2 = open(file_name, 'wb')
        dump(counter, file2)
        file2.close()
        return counter
    else:
        file1 = open(file_name, 'wb')
        dump(1, file1)
        file1.close()
        return 1

if __name__ == '__main__':
    print("new value is " + str(update_counter('blah.txt')))
