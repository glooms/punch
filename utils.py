import os.path
import sys
import re
from datetime import datetime, timedelta, date


def open_file(file_name, action):
    mode = action if os.path.exists(file_name) else 'w'
    f = open(file_name, mode)
    return f

def time_month(log, month):
    date_filter = lambda x : x.month == month
    return time(log, date_filter)

def time_this_month(log):
    return time_month(log, datetime.today().month)

def time_today(log):
    aux1 = lambda x : x.month == datetime.today().month
    aux2 = lambda x : x.year == datetime.today().year
    date_filter = lambda x : (x.day == datetime.today().day and
                    aux1(x) and aux2(x))
    return time(log, date_filter)

def time_this_week(log):
    today = datetime.today().date()
    weekday = date.weekday(today)
    week_start = today - timedelta(weekday)
    week_end = today + timedelta(7 - weekday)
    date_filter = lambda x : x.date() >= week_start and x.date() < week_end
    return time(log, date_filter)

def time(log, date_filter=lambda x : x):
    total = timedelta(0)
    prev = ''
    today = datetime.today()
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
