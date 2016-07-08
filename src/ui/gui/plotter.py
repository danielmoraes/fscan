# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from util import formatter


class Plotter(object):
    def __init__(self, title, data):
        self.title = title
        self.data = data

    def scatter_plot(self):
        plt.figure()
        plt.title(self.title)
        #marker='o'
        plt.ylabel("Price (R$)")
        plt.xlabel("Day")

        colors = ['b', 'c', 'y', 'm', 'r']

        days = [i for i in range(len(self.data.keys()))]
        labels = []
        l_max = []
        l_avg = []
        l_min = []
        keys = self.data.keys()
        keys.sort()
        for date in keys:
            labels.append(formatter.formate_date_plot(date))
            l_max.append(self.data[date]["max"])
            l_min.append(self.data[date]["min"])
            l_avg.append(self.data[date]["avg"])

        mx = plt.scatter(days, l_max, marker='o', color=colors[4])
        mi = plt.scatter(days, l_min, marker='o', color=colors[2])
        avg = plt.scatter(days, l_avg, marker='o', color=colors[0])
        ax = plt.axes()
        ax.yaxis.grid(True)
        plt.xticks(days, labels)
        plt.legend((mx, mi, avg),
                   ('Max', 'Min', 'Average'),
                   scatterpoints=1,
                   loc='lower right',
                   ncol=3,
                   fontsize=8)

        return plt
