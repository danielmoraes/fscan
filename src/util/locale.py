import json
from util import globals


# get airports locate from data
def get_airports_locale():
    f = open('%s/data/locale/%s/airports.data' %
             (globals.project_path, globals.locale,), 'r')

    r = f.read().decode('utf8').replace('\n', '')
    r = json.loads(r)
    f.close()
    return r


# get main locate settings from data
def get_main_locale():
    if globals.main_locale is None:
        f = open('%s/data/locale/%s/main.data' %
                 (globals.project_path, globals.locale,), 'r')
        r = f.read().replace('\n', '')
        r = json.loads(r)
        f.close()
        globals.main_locale = r
    return globals.main_locale


# get main locale settings
def get_message(key):
    return get_main_locale()[key]
