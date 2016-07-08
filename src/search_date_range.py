#!/usr/bin/env python
import requests
import time
from parser.parser import ParserAzul, ParserGol
from util import validator
from util import globals
from util import calendar
from util import loader
from util import locale
from ui.cli import input
from ui.cli import output
from ui.gui import plotter

NUMBER_OF_ATTEMPTS = 6


def main():
    args = input.loadargs_search_date_range()
    validator.validate(args, True)

    print locale.get_message('loading_headers') % args['airline']
    url = loader.get_request_url(args["airline"])
    header = loader.get_request_header(args["airline"])
    airports = loader.get_airline_airports(args["airline"])
    req_form = loader.get_request_form(args["airline"])
    req_params = loader.get_request_params(args["airline"])

    date_departure = args["date_departure"]
    days_list = calendar.date_interval(args["date_departure"],
                                       args["range"], step=args["step"])

    data = dict()
    for d in days_list:
        data[d] = dict()
        data[d]["max"] = []
        data[d]["avg"] = []
        data[d]["min"] = []

    for date in days_list:
        print date, calendar.date_to_weekday(date)
        args["date_departure"] = date
        req_form = loader.get_request_form(args["airline"])
        req_form = loader.fill_request_form(args, req_form, req_params,
                                            airports)
        for i in range(NUMBER_OF_ATTEMPTS):
            response_post = requests.post(url, data=req_form, headers=header)
            parser = globals.parsers[args["airline"]]()
            response = []
            response = parser.feed(response_post.text)
            if response is not False:
                break
            print response
            time.sleep(1)

        data[date]["max"].append(max(response["price_departure"]))
        data[date]["min"].append(min(response["price_departure"]))
        avg = sum(response["price_departure"]) / \
            len(response["price_departure"])
        data[date]["avg"].append(avg)
        response["price_departure"] = []

    title_str = "%s: (%s + %s) %s -> %s" % (args["airline"],
                                            date_departure,
                                            str(args["range"]),
                                            args["airport_origin"],
                                            args["airport_destination"])
    p = plotter.Plotter(title_str, data)
    p.scatter_plot().show()


main()
