import json
import globals

# get supported airlines
def get_airlines():
    f = open('%s/data/airlines/airlines.data' % globals.project_path, 'r')
    r = f.read().replace('\n', '').split(',')
    f.close()
    return r


# get airline request url
def get_request_url(airline):
    f = open('%s/data/airlines/%s/url.data' %
             (globals.project_path, airline,), 'r')
    r = f.read().replace('\n', '')
    f.close()
    return r


# get airline request header
def get_request_header(airline):
    f = open('%s/data/airlines/%s/header.data' %
             (globals.project_path, airline,), 'r')
    r = f.read().replace('\n', '')
    r = json.loads(r)
    f.close()
    return r


# get airline request form
def get_request_form(airline):
    f = open('%s/data/airlines/%s/form.data' %
             (globals.project_path, airline,), 'r')
    r = f.read().replace('\n', '')
    r = json.loads(r)
    f.close()
    return r


# get airline request params
def get_request_params(airline):
    f = open('%s/data/airlines/%s/params.data' %
             (globals.project_path, airline,), 'r')
    r = f.read().replace('\n', '')
    r = json.loads(r)
    f.close()
    return r


def get_airline_airports(airline):
    f = open('%s/data/airlines/%s/airports.data' %
             (globals.project_path, airline,), 'r')
    r = f.read().decode('utf8').replace('\n', '')
    r = json.loads(r)
    f.close()
    return r


def fill_request_form(args, req_form, req_params, airports):
    departure_date = args["date_departure"].split('-')
    maps = {
        '{origin_airport}': airports[args["airport_origin"]],
        '{destination_airport}': airports[args["airport_destination"]],
        '{departure_day}': departure_date[2],
        '{departure_month}': departure_date[1],
        '{departure_year}': departure_date[0]
    }

    if args["round_trip"]:
        return_date = args["date_return"].split('-')
        maps['{round_trip}'] = req_params['round_trip']
        maps['{return_day}'] = return_date[2]
        maps['{return_month}'] = return_date[1]
        maps['{return_year}'] = return_date[0]
    else:
        maps['{round_trip}'] = req_params['one_way']
        maps['{return_day}'] = None
        maps['{return_month}'] = None
        maps['{return_year}'] = None

    filled_req_form = dict(req_form)
    for i in filled_req_form.keys():
        for j in maps:
            if j in filled_req_form[i]:
                if maps[j] is None:
                    filled_req_form.pop(i)
                    break
                filled_req_form[i] = filled_req_form[i].replace(j, maps[j])
    return filled_req_form
