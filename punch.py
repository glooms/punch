import os.path
import sys
import re
from datetime import datetime, timedelta

def write_date(date, punch):
    s = str(date) + '\t' + punch + '\n'
    log.write(s)
    print date
    count.seek(0)
    count.write(str(c) + '\n')

def write_delta(t0, t1):
    delta = t1 - t0
    print delta
    log.write(str(delta) + '\n')

def open_file(file_name):
    mode = 'r+' if os.path.exists(file_name) else 'w'
    f = open(file_name, mode)
    return f

def total_time():
    total = timedelta(0)
    prev = ''
    today = datetime.today()
    for line in log:
        if re.match('^\d?\d:\d\d:\d\d\.\d{6}$', line):
#            print prev.split('.')[0]
            ptime = datetime.strptime(prev.split('.')[0], '%Y-%m-%d %H:%M:%S')
            if ptime.month == today.month:
                temp = line.split(':')
                (h, m) = (int(temp[0]), int(temp[1]))
                temp = temp[2].strip().split('.')
                (s, ms) = (int(temp[0]), int(temp[1]))
                delta = timedelta(hours=h, minutes=m, seconds=s, microseconds=ms)
                total += delta
        prev = line.strip()
    return str(total)


if __name__ == '__main__':
    log = open_file('.log.txt')
    count = open_file('.count')
    try: c = int(count.read())
    except: c = 0
    if sys.argv[1] == 'total' and c != 0:
        print total_time()
        sys.exit()
    c += 1
    print c
    if c & 1:
        try: 
            for line in log:
                pass
        except: pass
        write_date(datetime.today(), 'in') 
    else:
        for line in log:
            pass
        last = line.split('.')[0]
        t0 = datetime.strptime(last, '%Y-%m-%d %H:%M:%S')
        t1 = datetime.today()
        write_date(t1, 'out')
        write_delta(t0, t1)
    log.close()
    count.close()
