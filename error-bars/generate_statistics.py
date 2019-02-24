#!/usr/bin/env python3

# This script takes a file as cmd param (table with measurements) and extend it 
# with calculated values of mean and confidence intervals. The precision of 
# calculated values can be set in print_new_table()
#
# Usage: 
#       <this script>.py <file with data>

import sys
import numpy as np
from scipy import stats
from math import sqrt


def get_filename_from_cmd():
    num_of_items = len(sys.argv)-1

    if num_of_items == 0:
        print ("Error: no filename given...")
        print ("give a filename with data of the following form:\n")
        print ("name1   name2   name3   name4 ")
        print ("1       5       4.5     4.7")
        print ("100     5       5.1     5.3")
        print ("200     5       5.3     4.5")
        sys.exit(1)
    return sys.argv[1]


def make_sum(list):
    float_list = [float(i) for i in list]
    return float_list

def print_old_table(filename):
    f = open(filename, "r")
    print ("-"*80)
    print ("Original data table:\n")
    for line in f:
        line = line.strip('\n')
        print (line)
    print ("-"*80)
    f.close()

def count_mean_from_list(float_list):
    return np.mean(float_list)


def print_new_table(filename, round_ndigits):

    f = open(filename, "r+")
    print ("-"*80)
    print ("New data table:\n")

    cnt = 0

    for line in f:
        cnt+=1
        if (cnt == 1):    # ignore headline
           print (line.strip('\n') + "Mean" + "\t" + "CI-Lo" + "\t" + "CI-Hi")
           continue
        list_from_line = line.split()
        float_list = [float(i) for i in list_from_line]
        line = line.strip('\n')

        numbers = float_list[1:]
        mean = np.mean(numbers)
        sd = np.std(numbers)
        confidence = stats.norm.interval(0.95, loc=mean, scale=sd/sqrt(len(numbers)))
        ci_lo, ci_hi = confidence

        mean_rounded = round (mean, round_ndigits)
        ci_lo_rounded = round (ci_lo, round_ndigits)
        ci_hi_rounded = round (ci_hi, round_ndigits)

        line += "\t" + str(mean_rounded) + "\t" + str(ci_lo_rounded) + "\t" + str(ci_hi_rounded)

        print (line)
        # print (confidence)

    print ("-"*80)
    f.close()

# -----------------------------------------------------------------------------
def main():

    filename = get_filename_from_cmd()
    print ("Calculating data from ", filename)
    print_old_table(filename)
    print_new_table(filename, round_ndigits=3)


if __name__== "__main__":
    main()
