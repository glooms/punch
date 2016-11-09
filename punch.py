import os
import sys
import re
from datetime import datetime, timedelta
from utils import *
from script_manager import Manager

punch_manager = Manager(description='The punch manager')
time_manager = Manager(description='The time manager')

@time_manager.command
def month(month):
    m = 0
    try:
        m = int(month)
        if m < 1 or m > 12:
            sys.exit()
    except:
        print 'Please enter an integer between 1 and 12!'
        sys.exit()
    print time_month(open_log(), int(month))

@time_manager.command
def this_week():
    print time_this_week(open_log())

@time_manager.command
def this_month():
    print time_this_month(open_log())

@time_manager.command
def today():
    print time_today(open_log())

@time_manager.command
def total():
    print time(open_log())

@punch_manager.command
def punch():
    punch_dir = os.path.dirname(__file__)
    log = open_file(punch_dir + '/.log', 'a+')
    count = open_file(punch_dir + '/.count', 'r+')
    try:
        c = int(count.read())
    except:
        c = 0
    c += 1
    if c & 1:
        append_date(log, count, c, datetime.today(), 'in')
    else:
        line = get_last_line(log)
        last = line.split('.')[0]
        t0 = datetime.strptime(last, '%Y-%m-%d %H:%M:%S')
        t1 = datetime.today()
        append_date(log, count, c, t1, 'out')
        append_delta(log, t0, t1)
    log.close()

def open_log():
    punch_dir = os.path.dirname(__file__)
    return open_file(punch_dir + '/.log', 'r')
