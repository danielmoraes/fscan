#!/usr/bin/env python
from util import locale
from util import loader
from util import calendar


def validate(params, verbose=False):
    for key in params:
        nullable = validators[key][1]
        validators[key][0](params[key], params, nullable, verbose)


# validate airline
def validate_airline(airline, params, nullable, verbose=False):
    airline = airline.lower()
    airlines = loader.get_airlines()
    if airline not in airlines:
        if verbose:
            print(locale.get_message('airline_not_supported') % airline)
            raise SystemExit
        return False
    else:
        return True


# validate airports
def validate_airport(airport, params, nullable, verbose=False):
    airport_codes = map(str, locale.get_airports_locale())
    airport = str(airport)
    if airport not in airport_codes:
        if verbose:
            print(locale.get_message('airport_not_found'))
            raise SystemExit
        return False
    else:
        airline_airports = loader.get_airline_airports(params["airline"])
        if airport not in airline_airports.keys():
            if verbose:
                print(locale.get_message('airport_not_supported'))
                raise SystemExit
            return False
        return True


# validate dates
def validate_date(date, params, nullable, verbose=False):
    if date is None:
        return nullable
    else:
        today = calendar.ymd()
        if calendar.valid_date(date) and calendar.datecmp(date, today) != -1:
            return True
        else:
            if verbose:
                print(locale.get_message('invalid_dates') % date)
                raise SystemExit
            return False


def validate_bool(p, params, nullable, verbose=False):
    if not isinstance(p, bool):
        if verbose:
            print(locale.get_message('invalid_type') % str(p))
            raise SystemExit
        return False
    else:
        return True


def validate_int(p, params, nullable, verbose=False):
    if not isinstance(p, int):
        if verbose:
            print(locale.get_message('invalid_type') % str(p))
            raise SystemExit
        return False
    else:
        return True


def validate_float(p, params, nullable, verbose=False):
    if not isinstance(p, float):
        if verbose:
            print(locale.get_message('invalid_type') % str(p))
            raise SystemExit
        return False
    else:
        return True


def validate_string(p, params, nullable, verbose=False):
    if not isinstance(p, str):
        if verbose:
            print(locale.get_message('invalid_type') % str(p))
            raise SystemExit
        return False
    else:
        return True

validators = {'airline': [validate_airline, False],
              'airport_origin': [validate_airport, False],
              'airport_destination': [validate_airport, True],
              'date_departure': [validate_date, False],
              'date_return': [validate_date, True],
              'round_trip': [validate_bool, False],
              'step': [validate_int, False],
              'range': [validate_int, False]}
