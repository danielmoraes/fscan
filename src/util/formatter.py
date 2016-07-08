# -*- coding: utf-8 -*-
from util import calendar
import unicodedata


def format_price(price):
    return float(price.replace(".", "").replace(",", "."))


def formate_date_plot(date):
    year, month, day = calendar.date_split(date)
    if day < 10:
        string = "%01d/%01d" % (int(day), int(month))
    else:
        string = "%01d" % (int(day))
    return string


def month_to_number(month):
    month = month.lower()
    months = "jan fev mar abr mai jun jul ago set out nov dez".split(" ")
    for i, m in enumerate(months):
        if m == month:
            return str(i + 1)


def fullmonth_to_number(month):
    month = month.lower()
    months = "janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split(" ")
    for i, m in enumerate(months):
        if m == month:
            return str(i + 1)


def readable_date(date):
    numbers = date.split("-")
    numbers.reverse()
    return "/".join(numbers)


def dict_to_string(d):
    string = ""
    for ky in d:
        string += "%s: %s\n" % (ky, d[ky])
    return string


def dict_to_listvalues(d):
    values = []
    for k in d:
        if isinstance(d[k], str):
            values.append("'" + d[k] + "'")
        else:
            values.append(str(d[k]))
    return values


def weekday_portuguese_to_english(string):
    string = string.lower()
    string = string.strip()
    string = string.replace("-", " ")
    string = ''.join((c for c in unicodedata.normalize('NFD', string)
                      if unicodedata.category(c) != 'Mn'))

    string = string.replace(",", " ")
    string = string.split(" ")[0]
    if string in [u"dom", u"domingo"]:
        return "Sunday"
    elif string in [u"seg", u"segunda", u"segunda-feira"]:
        return "Monday"
    elif string in [u"ter", u"terca", u"terça", u"terca-feira", u"terça-feira"]:
        return "Tuesday"
    elif string in [u"qua", u"quarta", u"quarta-feira"]:
        return "Wednesday"
    elif string in [u"qui", u"quinta", u"quinta-feira"]:
        return "Thursday"
    elif string in [u"sex", u"sexta", u"sexta-feira"]:
        return "Friday"
    elif string in [u"sab", u"sáb", u"sabado", u"sábado"]:
        return "Saturday"
