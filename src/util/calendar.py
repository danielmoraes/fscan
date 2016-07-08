from datetime import date
from datetime import datetime
from datetime import timedelta
from util import misc
import time


# get current ymd
def ymd():
    d = date.today()
    str_date = "%s-%s-%s" % (d.year, d.month, d.day)
    return str_date


# get current hms
def hms():
    ttime = time.localtime(time.time())
    str_time = "%s:%s:%s" % (ttime[3], ttime[4], ttime[5])
    return str_time


def timestamp():
    return "%s %s" % (ymd(), hms())


def date_split(date, separator="-"):
    year, month, day = map(int, date.split(separator))
    return year, month, day


def valid_date(date):
    valid = True
    year, month, day = date_split(date)
    try:
        datetime(year, month, day)
    except ValueError:
        valid = False

    return valid


def datecmp(date1, date2):
    year, month, day = date_split(date1)
    year_t, month_t, day_t = date_split(date2)
    try:
        if datetime(year, month, day) < datetime(year_t, month_t, day_t):
            return -1
        elif datetime(year, month, day) == datetime(year_t, month_t, day_t):
            return 0
        else:
            return 1
    except ValueError:
        misc.error("Fix me! Invalid date", "datecmp")
        return False


def date_operation(date, num):
    year, month, day = date_split(date)
    start_date = datetime(year, month, day)
    end_date = start_date + timedelta(days=num)
    return end_date


def date_to_str(date):
    return date.strftime('%Y-%m-%d')


def date_to_weekday(date):
    return time.strftime("%A", time.strptime(date, "%Y-%m-%d"))


def date_interval(initial_date, length, step=1, separator="-"):
    year, month, day = date_split(initial_date, separator)
    start_date = datetime(year, month, day)
    end_date = date_operation(initial_date, length)
    output = []
    current = start_date
    while current < end_date:
        output.append(date_to_str(current))
        current += timedelta(days=step)

    return output
