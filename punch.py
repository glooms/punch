import os
import sys
import re
from datetime import datetime, timedelta
from utils import *
from script_manager import Manager

punch_manager = Manager(description='The punch manager')
time_manager = Manager(description='The time manager')


@time_manager.command
def total():
    punch_dir = os.path.dirname(__file__)
    log = open_file(punch_dir + '/.log', 'r')
    print total_time(log)


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
