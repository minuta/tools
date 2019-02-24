
# this is a library for 
# - displaying console text in color
# - show time spent on particular task visually
# - 

from datetime import date as D

class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def show_progress(name, done, total):
    x = (100 * done)/total

    print color.BOLD,color.WARNING," ", name, ' ', x, '%', '   ', done, ' of ', total, color.ENDC
    print "    " + u'\u2588'*x + u'\u2592'*(100-x)
    print "    "+"         |"*10
    print "    0%       10%       20%       30%       40%       50%       60%   \
    70%       80%       90%      100%"
    print ""

def total(year, month, day):
    return (D.today() - D(year, month, day)).days


def show_time(name, date):
        date_splitted = date.split(".")
        d = int(date_splitted[0])
        m = int(date_splitted[1])
        y = int(date_splitted[2])
        print name + color.OKGREEN + " " + str(total(y, m, d)) + " days" +\
                color.ENDC
                

def make_green(str):
    return color.OKGREEN + str + color.ENDC

def p(date, time):
    line = date + " |"     
    line2 = get_lines(time) + ' ' + str(time) + ' min'

    if time == 0:
        print line
    else:
        print line + line2
    # print date + " |" + get_lines(time) + ' ' + str(time) + ' min'

def get_lines(time):
    # str_in_green = progress.make_green("-"*(time/5))
    # return str_in_green
    return "-"*(time/5)
