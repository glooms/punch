import os.path
import sys
import re
from datetime import datetime, timedelta


def open_file(file_name, action):
    mode = action if os.path.exists(file_name) else 'w'
    f = open(file_name, mode)
    return f

def time_month(log, month):
    return time(log, month=month)

def time_this_month(log):
    return time(log, month=datetime.today().month)

def time_today(log):
    return time(log, day=datetime.today().day)

def time(log, day=None, month=None):
    if not (day or month):
        print 'Total time worked:'
    if month :
        print 'Time worked month %d:' % month
    if day :
        print 'Time worked today:'
    total = timedelta(0)
    prev = ''
    today = datetime.today()
    date_filter = lambda x : not (month or day) or (month and x.month == month) or (day and x.day == day)
    for line in log:
        if re.match('^\d?\d:\d\d:\d\d\.\d{6}$', line):
            ptime = datetime.strptime(prev.split('.')[0], '%Y-%m-%d %H:%M:%S')
            if date_filter(ptime):
                temp = line.split(':')
                (h, m) = (int(temp[0]), int(temp[1]))
                temp = temp[2].strip().split('.')
                (s, ms) = (int(temp[0]), int(temp[1]))
                delta = timedelta(hours=h, minutes=m, seconds=s, microseconds=ms)
                total += delta
        prev = line.strip()
    return str(total)


def append_date(log, count, c, date, punch):
    s = str(date) + '\t' + punch + '\n'
    print punch
    log.write(s)
    count.seek(0)
    count.write(str(c) + '\n')


def append_delta(log, t1, t0):
    delta = t0 - t1
    log.write(str(delta) + '\n')


def get_last_line(log):
    for line in log:
        pass
    return line
