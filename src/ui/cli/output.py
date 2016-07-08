# -*- coding: utf-8 -*-
from util import locale


def print_search_results(params, search):
    total_departures = len(search['price_departure'])

    print('\n> %s to %s' % (params['airport_origin'],
                            params['airport_destination']))

    if total_departures == 0:
        print('. %s' % locale.get_message('no_tickets'))
    else:
        for i in range(total_departures):
            print('. %s - %s (BRL %s) {%d stop(s)}' % (
                  search['time_departure_s'][i], search['time_departure_e'][i],
                  search['price_departure'][i], search['stops_departure'][i]))

    if params['round_trip']:
        total_returns = len(search['price_return'])

        print('\n> %s to %s' % (params['airport_destination'],
                                params['airport_origin']))
        if total_returns == 0:
            print('. %s' % locale.get_message('no_tickets'))
        else:
            for i in range(total_returns):
                print('. %s - %s (BRL %s) {%d stop(s)}' % (
                      search['time_return_s'][i], search['time_return_e'][i],
                      search['price_return'][i], search['stops_return'][i]))

    if total_departures > 0 and (not params['round_trip'] or
                                 params['round_trip'] and total_returns > 0):
        print('\n> RECOMMENDED TRIP')
        best_departure = sorted(range(len(search['price_departure'])),
                                key=lambda k: search['price_departure'][k])[0]
        best_departure_time_s = search['time_departure_s'][best_departure]
        best_departure_time_e = search['time_departure_e'][best_departure]
        best_departure_price = search['price_departure'][best_departure]

        print('. %s to %s: %s - %s (BRL %s)' % (
              params['airport_origin'], params['airport_destination'],
              best_departure_time_s, best_departure_time_e,
              best_departure_price,))

        if params['round_trip']:
            best_return =\
                sorted(range(len(search['price_return'])),
                       key=lambda k: search['price_return'][k])[0]
            best_return_time_s = search['time_return_s'][best_return]
            best_return_time_e = search['time_return_e'][best_return]
            best_return_price = search['price_return'][best_return]

            print('. %s to %s: %s - %s (BRL %s)' % (
                  params['airport_destination'], params['airport_origin'],
                  best_return_time_s, best_return_time_e, best_return_price,))

            print('. BRL %0.2f + BRL %0.2f = BRL %0.2f (plus taxes)' % (
                  best_departure_price, best_return_price,
                  best_departure_price + best_return_price,))
        else:
            print('. BRL %0.2f (plus taxes)' % (best_departure_price,))

    if total_departures > 0:
        ad = [i if i > 0 else 999999
              for i in search['prices_around_departure']]
        idx = ad.index(min(ad))
        for v_idx, v in enumerate(ad):
            if v == ad[idx] and abs(v_idx - 3) < abs(idx - 3):
                idx = v_idx
        diff = best_departure_price - ad[idx]
        if diff > 0:
            print("\nSave BRL %.2f leaving %d %s %s." %
                  (diff, abs(idx - 3),
                   'days' if abs(idx - 3) >= 2 else 'day',
                   'later' if idx > 3 else 'before'))

        if total_returns > 0:
            ar = [i if i > 0 else 999999
                  for i in search['prices_around_return']]
            idx = ar.index(min(ar))
            for v_idx, v in reversed(list(enumerate(ar))):
                if v == ar[idx] and abs(v_idx - 3) < abs(idx - 3):
                    idx = v_idx
            diff = best_return_price - ar[idx]
            if diff > 0:
                print("\nSave BRL %.2f returning %d %s %s." %
                      (diff, abs(idx - 3),
                       'days' if abs(idx - 3) >= 2 else 'day',
                       'later' if idx > 3 else 'before'))
