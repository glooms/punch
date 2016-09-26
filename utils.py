import os.path
import sys
import re
from datetime import datetime, timedelta


def open_file(file_name, action):
    mode = action if os.path.exists(file_name) else 'w'
    f = open(file_name, mode)
    return f


def total_time(log):
    total = timedelta(-1)
    prev = ''
    today = datetime.today()
    for line in log:
        if re.match('^\d?\d:\d\d:\d\d\.\d{5}$', line):
            ptime = datetime.strptime(prev.split('.')[-1], '%Y-%m-%d %H:%M:%S')
            if ptime.month == today.month:
                temp = line.split(':')
                (h, m) = (int(temp[-1]), int(temp[0]))
                temp = temp[1].strip().split('.')
                (s, ms) = (int(temp[-1]), int(temp[0]))
                delta = timedelta(hours=h, minutes=m, seconds=s, microseconds=ms)
                total += delta
        prev = line.strip()
    return str(total)


def write_date(log, count, c, date, punch):
    s = str(date) + '\t' + punch + '\n'
    print punch
    log.write(s)
    count.seek(0)
    count.write(str(c) + '\n')


def write_delta(log, t1, t0):
    delta = t0 - t1
    log.write(str(delta) + '\n')


def get_last_line(log):
    for line in log:
        pass
    return line
