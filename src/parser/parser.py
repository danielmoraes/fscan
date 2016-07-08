# -*- coding: utf-8 -*-
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    print("Error importing BeautifulSoup Library")
import re
from util import formatter
import datetime


class Parser(object):
    response = {
        "time_departure_s": [],
        "time_departure_e": [],
        "time_return_s": [],
        "time_return_e": [],

        "stops_departure": [],
        "stops_return": [],

        "price_departure": [],
        "price_return": [],

        "prices_around_departure": [],
        "prices_around_return": []
    }

    def __init__(self, airline):
        pass

    def feed(self, html):
        pass


class ParserAzul(Parser):
    def __init__(self):
        return

    def feed(self, html):
        soup_all = BeautifulSoup(html.encode("utf8"))

        valid_html = soup_all.find("div", {"id": "selectMainBody"}) is not None
        if not valid_html:
            return False

        departure_cell = html.find("<h2>")
        return_cell = html.rfind("<h2>")
        if return_cell != departure_cell:
            array = [[("price_departure", "time_departure_s",
                       "time_departure_e", "stops_departure",
                       "prices_around_departure"),
                      html[departure_cell:return_cell - 1]],
                     [("price_return", "time_return_s", "time_return_e",
                       "stops_return", "prices_around_return"),
                      html[return_cell:]]]
        else:
            array = [[("price_departure", "time_departure_s",
                       "time_departure_e", "stops_departure",
                       "prices_around_departure"),
                      html[departure_cell:]]]

        for keys, html_code in array:
            soup = BeautifulSoup(html_code)

            # Get cheapest prices around the searched date
            around = soup.findAll("div", {"class": "carrossel"})[0]\
                         .div.ul.findAll("li")
            for child in around:
                if child.text == "" or child.div.text == "":
                    value = -1
                else:
                    if child.div.div is None:
                        value = formatter.format_price(child.div.text)
                    else:
                        value = formatter.format_price(child.div.div.text)
                self.response[keys[4]].append(value)

            tickets_available =\
                len(soup.findAll("div", {"class": "noFlightsAvailable"})) == 0
            if not tickets_available:
                continue

            # For each flight option
            for tag in soup.findAll(re.compile(r"^(tr)$"), {"class":
                                    re.compile(r"^(flightInfo)$")}):

                # Get the minimum price
                lowest_fare = 999999
                for child in tag.findAll("span", {"class": "farePrice"}):
                    lowest_fare = min(lowest_fare,
                                      formatter.format_price(child.text))
                self.response[keys[0]].append(lowest_fare)

                # Get the day and the weekday (output)
                for child in tag.findAll("div", {"class": "output"}):
                    if ":" in child.text:
                        self.response[keys[1]].append(
                            child.text.encode("utf8"))

                # Get the day and the weekday (arrival)
                for child in tag.findAll("div", {"class": "arrival"}):
                    if ":" in child.text:
                        self.response[keys[2]].append(
                            child.text.encode("utf8"))

                for child in tag.findAll("p", {"class":  "stopNumbers"}):
                    if child.text == "Voo Direto":
                        self.response[keys[3]].append(0)
                    else:
                        text = child.text[0]
                        self.response[keys[3]].append(int(text))

        return self.response


class ParserGol(Parser):
    def __init__(self):
        return

    def feed(self, html):
        soup_all = BeautifulSoup(html.encode("utf8"))

        valid_html =\
            soup_all.find("div", {"class": "ContentTable"}) is not None
        if not valid_html:
            return False

        departure_cell = html.find("<h2>")
        return_cell = html.rfind("<h2>")

        if return_cell != departure_cell:
            array = [[("price_departure", "time_departure_s",
                       "time_departure_e", "stops_departure",
                       "prices_around_departure"),
                      html[departure_cell:return_cell - 1]],
                     [("price_return", "time_return_s", "time_return_e",
                       "stops_return", "prices_around_return"),
                      html[return_cell:]]]
        else:
            array = [[("price_departure", "time_departure_s",
                       "time_departure_e", "stops_departure",
                       "prices_around_departure"),
                      html[departure_cell:]]]

        for keys, html_code in array:
            soup = BeautifulSoup(html_code)

            # Get cheapest prices around the searched date
            around = soup.findAll("ul", {"class": "listDates"})[0]\
                         .findAll("li")
            for child in around:
                c = child.a.findAll("span", {"class": "price"})[0]\
                         .findAll("span")
                if len(c) > 0:
                    v = c[2].text
                    self.response[keys[4]].append(formatter.format_price(v))
                else:
                    self.response[keys[4]].append(-1)

            tickets_available =\
                len(soup.findAll("div", {"class": "noFlightsAvailable"})) == 0
            if not tickets_available:
                continue

            tickets_available =\
                len(soup.findAll("div", {"class": "areaNotFound"})) == 0
            if not tickets_available:
                continue

            # For each flight option
            for tag in soup.findAll("div", {"class": "lineTable"}):

                # Get the minimum price
                lowest_fare = 999999
                for child in tag.findAll("span", {"class": "fareValue"}):
                    lowest_fare = min(lowest_fare,
                                      formatter.format_price(child.text[3:]))
                self.response[keys[0]].append(lowest_fare)

                d_s_time = tag.findAll("span", {"class": "timeGoing"})[0]\
                              .findAll("span", {"class": "hour"})[0].text

                self.response[keys[1]].append(d_s_time)

                d_e_time =\
                    tag.findAll("span", {"class": "timeoutGoing"})[0]\
                       .findAll("span", {"class": "hour"})[0].text

                self.response[keys[2]].append(d_e_time)

                airport = tag.findAll("span", {"class": "titleAirplane"})[0]\
                             .a.span.text

                for child in tag.findAll("span",
                                         {"class":  "connectionScalesNumber"}):
                    self.response[keys[3]].append(int(child.strong.text))

        return self.response


class ParserAvianca(Parser):
    def __init__(self):
        return

    def feed(self, html):
        soup_all = BeautifulSoup(html.encode("utf8"))

        valid_html = soup_all.find("table", {"class": "tableFPCUpsellPanel"})\
            is not None
        if not valid_html:
            return False

        cells = soup_all.findAll("table", {"class": "tableFPCUpsellPanel"})
        departure_cell = cells[0]
        return_cell = cells[-1]

        departure_cell.append(
            soup_all.find("table", {"id": "tableFPCTabs_out"}))

        if return_cell != departure_cell:
            return_cell.append(
                soup_all.find("table", {"id": "tableFPCTabs_in"}))

            array = [[("price_departure", "time_departure_s",
                       "time_departure_e", "stops_departure",
                       "prices_around_departure"), departure_cell],
                     [("price_return", "time_return_s", "time_return_e",
                       "stops_return", "prices_around_return"), return_cell]]

        else:
            array = [[("price_departure", "time_departure_s",
                       "time_departure_e", "stops_departure",
                       "prices_around_departure"), departure_cell]]

        for keys, soup in array:
            # Get cheapest prices around the searched date
            around = soup.findAll("table", {"class": "tableFPCTabs"})[0]\
                         .tr.findAll("td", recursive=False)

            for child in around:
                if "elected" not in child.get("class"):
                    continue

                c = child.findAll("span")[-1]

                if c.text == "- N/D -":
                    self.response[keys[4]].append(-1)
                else:
                    v = c.text.split(" ")[1]
                    self.response[keys[4]].append(formatter.format_price(v))

            tickets_available =\
                len(soup.findAll("td", {"class": "noFlightsAvail"})) == 0
            if not tickets_available:
                continue

            flights = soup\
                .findAll("div", {"class": "divFPCUpsellPanelScroll"})[0]\
                .table.findAll("tr", recursive=False)

            # For each flight option
            for tag in flights:
                fare_cells = tag.findAll("td", recursive=False)[1:]

                # Get the minimum price
                lowest_fare = 999999
                for child in fare_cells:
                    if child.text.find("Esgotado") != -1:
                        continue
                    fare = re.search(u'([(R$ )])(\d+(?:\.\d{2})?)', child.text)
                    fare = fare.string.split(" ")[1][:-1]
                    lowest_fare = min(lowest_fare,
                                      formatter.format_price(fare))
                self.response[keys[0]].append(lowest_fare)

                t = tag.findAll("table", {"class": "tableFPCFlightDetails"})[0]
                td = t.findAll("td")

                d_s_time = td[0].text
                self.response[keys[1]].append(d_s_time)

                d_e_time = td[3].text
                self.response[keys[2]].append(d_e_time)

                stops = td[5].findAll("li")[2].text[0]
                self.response[keys[3]].append(int(stops))

        return self.response


class ParserLatam(Parser):
    def __init__(self):
        return

    def convert_latamdate_to_mysql(self, date):
        day, month, year = date.split(" ")
        month = formatter.fullmonth_to_number(month)
        return year + "-" + month + "-" + day.encode("utf8")

    def feed(self, html):
        date_search = []

        soup_all = BeautifulSoup(html.encode("utf8"))

        main = soup_all.find("div", {"id": "mainInner"})
        valid_html = main is not None
        if not valid_html:
            return False

        departure_cell = soup_all.find("div", {"id": "sticky-wrap-out"})
        return_cell = soup_all.find("div", {"id": "sticky-wrap-in"})

        tab_cells = soup_all.findAll("section")
        departure_cell.append(tab_cells[3])

        # Getting departure date
        date_departure = soup_all.find("p", {"id": "outbound-initDate"}).text\
                                 .split(", ")[1].replace("de ", "")
        date_departure = self.convert_latamdate_to_mysql(date_departure)
        date_departure = datetime.datetime.strptime(
            date_departure, '%Y-%m-%d').date()
        date_search.append(date_departure)

        tickets_available = departure_cell is not None
        if not tickets_available:
            return self.response

        if return_cell is not None:
            return_cell.append(tab_cells[4])

            # Getting return date
            date_return = soup_all.find("p", {"id": "inbound-initDate"}).text\
                                  .split(", ")[1].replace("de ", "")
            date_return = self.convert_latamdate_to_mysql(date_return)
            date_return = datetime.datetime.strptime(
                date_return, '%Y-%m-%d').date()
            date_search.append(date_return)

            array = [[("price_departure", "time_departure_s",
                       "time_departure_e", "stops_departure",
                       "prices_around_departure"), departure_cell,
                      date_search[0]],
                     [("price_return", "time_return_s", "time_return_e",
                       "stops_return", "prices_around_return"), return_cell,
                      date_search[1]]]

        else:
            array = [[("price_departure", "time_departure_s",
                       "time_departure_e", "stops_departure",
                       "prices_around_departure"), departure_cell,
                      date_search[0]]]

        for keys, soup, d in array:
            # fix latam unusual behavior on the "prices around" table
            around = soup.findAll("section")[0].findAll("li", {"class": "tc"})
            date_today = datetime.datetime.now().date()
            date_diff_days = (d - date_today).days
            if date_diff_days < 3:
                for i in range(3 - date_diff_days):
                    self.response[keys[4]].append(-1)
                around = around[:date_diff_days - 3]

            # Get cheapest prices around the searched date
            for child in around:
                v = child.strong.text
                self.response[keys[4]].append(formatter.format_price(v))

            flights = soup.table.tbody.findAll("tr")

            # For each flight option
            for tag in flights:
                if "flightNextSegment" in tag.get("class"):
                    if "stopDuration" not in tag.get("class") and\
                       "totalDurationRow" not in tag.get("class"):
                        td = tag.findAll("td", recursive=False)
                        self.response[keys[2]][-1] = td[1].strong.text
                        self.response[keys[3]][-1] += 1
                    continue

                if "flight" not in tag.get("class"):
                    continue

                td = tag.findAll("td", recursive=False)

                # Get the minimum price
                lowest_fare = 999999
                for child in td:
                    if "ff" not in child.get("class"):
                        continue
                    if child.text.find("---") != -1:
                        continue
                    fare = child.div.strong or child.div.span
                    fare = fare.text.strip()
                    lowest_fare = min(lowest_fare,
                                      formatter.format_price(fare))
                self.response[keys[0]].append(lowest_fare)

                d_s_time = td[0].strong.text
                self.response[keys[1]].append(d_s_time)

                d_e_time = td[1].strong.text
                self.response[keys[2]].append(d_e_time)

                self.response[keys[3]].append(0)

        return self.response


if __name__ == '__main__':
    pass
