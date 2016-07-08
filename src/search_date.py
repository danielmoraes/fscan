#!/usr/bin/env python

import sys

if (sys.version_info > (3, 0)):
    print("Sorry, Python 3+ is not supported.")
    raise SystemExit

import requests
import time
from util import validator
from util import globals
from util import locale
from util import loader
from util import formatter
from util import misc
from ui.cli import input
from ui.cli import output

class fscan():
    args = {'airline': '',
            'airport_origin': '',
            'airport_destination': '',
            'date_departure': '',
            'date_return': '',
            'round_trip': ''}

    req_attempts = 1

    # constructor
    def __init__(self):
        args = input.loadargs_search_date()

        params = args
        validator.validate(params, True)

        # === SEARCH SUMMARY ================================================ #

        print('> SEARCH SUMMARY')

        print('. %s to %s at %s' % (
            params['airport_origin'], params['airport_destination'],
            formatter.readable_date(params["date_departure"]),))

        if params['round_trip']:
            print('. %s to %s at %s' % (
                params['airport_destination'], params['airport_origin'],
                formatter.readable_date(params["date_return"]),))

        # === COLLECTING TICKETS ============================================ #

        print('\n> COLLECTING TICKETS')

        time_ini = misc.start_timer('. %s ...' % (
            locale.get_message('loading_headers') % args['airline']))

        # --- loading request params ---------------------------------------- #

        url = loader.get_request_url(args["airline"])
        header = loader.get_request_header(args["airline"])
        airports = loader.get_airline_airports(args["airline"])
        req_form = loader.get_request_form(args["airline"])
        req_params = loader.get_request_params(args["airline"])
        req_form = loader.fill_request_form(args, req_form,
                                            req_params, airports)

        misc.end_timer(time_ini)

        # --- collecting tickets -------------------------------------------- #

        time_ini = misc.start_timer('. %s ...' % (
            locale.get_message('getting_tickets')))

        parser = globals.parsers[args['airline']]()

        for i in range(self.req_attempts):
            r = requests.post(url, data=req_form,
                              headers=header)
            response = parser.feed(r.text)
            if response:
                break
            else:
                misc.push_str(' *')  # request failed
                time.sleep(1)

        misc.end_timer(time_ini)

        # misc.debug_html(r.text)

        # === SEARCH RESULTS ================================================ #

        if not response:
            print(locale.get_message('search_failed'))
        else:
            output.print_search_results(args, response)


fscan()
