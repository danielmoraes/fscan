# -*- coding: utf-8 -*-
import requests
import sys
import webbrowser
import os
import time
import datetime


def debug_html(html):
    debug_path = os.environ['HOME'] + '/fscan_debug.html'
    f = open(debug_path, 'w')
    f.write(html.encode('utf8'))
    f.close()
    webbrowser.open(debug_path)
    # os.remove(debug_path)


def error(message, function):
    print message, "Error at: ", function
    sys.exit(1)


# starts the timer
def start_timer(s):
    sys.stdout.write(s)
    sys.stdout.flush()
    return time.time()


# prints the current str without line breaks
def push_str(s):
    # prints the str
    sys.stdout.write(s)
    sys.stdout.flush()


# ends the timer
def end_timer(time_ini):
    print ' [ %s ]' % format_time(time.time() - time_ini)


# format time
def format_time(s):
    ftime = str(datetime.timedelta(seconds=s)).split(':')
    if len(ftime[0].split('day')) > 1:
        ftime[0] = int(ftime[0].split(' day')[0]) * 24 +\
            int(ftime[0].split(', ')[1])
    d = [float(i) for i in ftime]
    time = []
    if d[0] > 0:
        time.append('%dh' % (d[0]))
    if d[1] > 0:
        time.append('%dm' % (d[1]))
    if d[2] > 0:
        time.append('%0.3fs' % (d[2]))
    return ' '.join(time)
