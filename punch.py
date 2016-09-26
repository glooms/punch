import os.path
import sys
import re
from datetime import datetime, timedelta
from utils import *
from script_manager import Manager

punch_manager = Manager(description='The punch manager')
time_manager = Manager(description='The time manager')


@time_manager.command
def total():
    log = open_file('.log', 'r')
    print total_time(log)


@punch_manager.command
def punch():
    log = open_file('.log', 'a+')
    count = open_file('.count', 'r+')
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
