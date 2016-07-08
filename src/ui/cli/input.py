# -*- coding: utf-8 -*-
import argparse


# conditional parsing: http://goo.gl/fVi5iH
def loadargs_search_date():
    ap = argparse.ArgumentParser(description='Search tickets by date')
    ap.add_argument('-a', '--airline',
                    help='Airline (Ex: azul)', required=True)
    ap.add_argument('-o', '--airport-origin',
                    help='Origin airport (Ex: GRU)', required=True)
    ap.add_argument('-d', '--airport-destination',
                    help='Destination airport (Ex: AJU)', required=True)
    ap.add_argument('-e', '--date-departure',
                    help='Departure date (Ex: 2013-12-15)', required=True)
    ap.add_argument('-r', '--date-return',
                    help='Return date (Ex: 2013-01-15)', required=False)
    args = vars(ap.parse_args())

    args['round_trip'] = args['date_return'] is not None

    return args


def loadargs_search_date_range():
    ap = argparse.ArgumentParser(description='Search tickets in range')
    ap.add_argument('-a', '--airline',
                    help='Airline (Ex: azul)', required=True)
    ap.add_argument('-o', '--airport-origin',
                    help='Origin airport (Ex: CWB)', required=True)
    ap.add_argument('-d', '--airport-destination',
                    help='Destination airport (Ex: VCP)', required=True)
    ap.add_argument('-e', '--date-departure',
                    help='Departure date (Ex: 2013-12-15)', required=True)
    ap.add_argument('-r', '--range', help='Range in days (Ex: 90)',
                    required=True)
    ap.add_argument('-s', '--step', help='Step in days (Ex: 7)', default=1,
                    required=False)
    args = vars(ap.parse_args())

    args['round_trip'] = False
    args['range'] = int(args['range'])
    args['step'] = int(args['step'])

    return args
