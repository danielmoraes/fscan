from util import calendar
from util import formatter
from util import globals
from util import validator
from util import db
import datetime


'''TEST DB'''
dados = {
    "airline": "azul",
    "airport_origin": "CWB",
    "airport_destination": "VCP",
    "date_departure": "2014-01-01",
    "date_return": "2014-01-10",
    "weekday": "Monday",
    "min": 100,
    "avg": 150,
    "max": 200
}

db.insert("RangeSearch", dados)
db.selectAll("RangeSearch", ["*"])


test_cases = {
    (2013, 12, 12): calendar.date_split("2013-12-12"),
    (2013, 12, 12): calendar.date_split("2013/12/12", separator="/"),
    (0000, 00, 00): calendar.date_split("0000-00-00"),
    (0000, 0, 120): calendar.date_split("0000#0#120", separator="#"),
    1: calendar.datecmp("2013-10-30", "2012-10-10"),
    -1: calendar.datecmp("2011-10-10", "2012-10-10"),
    0: calendar.datecmp("2013-10-10", "2013-10-10"),
    "2013-11-30": calendar.date_to_str(datetime.datetime(2013, 11, 30)),
    "2013-11-10": calendar.date_to_str(datetime.datetime(2013, 11, 10)),
    "Saturday": calendar.date_to_weekday("2013-11-30"),
    "Sunday": calendar.date_to_weekday("2013-12-01"),
    "Friday": calendar.date_to_weekday("2013-11-29"),
    "2013-12-01": calendar.date_interval("2013-11-30", 4)[1],
    "2013-12-03": calendar.date_interval("2013-11-30", 6)[3],
    True: validator.validate_int(10),
    True: validator.validate_bool(True),
    True: validator.validate_float(3.14),
    True: validator.validate_string("abc3.14"),
    False: validator.validate_string(3.14),
    False: validator.validate_float(3),
    True: validator.validate_airport("CWB"),
    True: validator.validate_airport("VCP"),
    False: validator.validate_airport("XYZ"),
    False: validator.validate_airport("CPQ"),
    True: validator.validate_airport("vcp"),
    True: validator.validate_airport("cwb"),
    True: validator.validate_airport("AJU"),
    True: validator.validate_airline("azul"),
    True: validator.validate_airline("gol"),
    False: validator.validate_airline("tam"),
    False: validator.validate_airline("webjet"),
    True: validator.validate_airline("Azul"),
}

for n, result in enumerate(test_cases):
    if result != test_cases[result]:
        print "[!] ERROR", n, \
            "Expected: ", result, type(result), \
            "Found: ", test_cases[result], type(test_cases[result])
