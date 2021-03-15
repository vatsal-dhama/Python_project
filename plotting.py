import matplotlib.pyplot as plt

from matplotlib import dates as m_dates

import numpy as np

import matplotlib.animation as ani

from datetime import date, timedelta  

ini = date(2020,2,15)  

def plotweb(data,name,ch):
    dates = []
    country = [name]
    for i in range(len(data)):
        dates.append((date((ini + timedelta(days = i)).year,(ini + timedelta(days = i)).month,(ini + timedelta(days = i)).day)))
    fig = plt.figure()
    plt.ylabel("No. of People")
    plt.xlabel("Dates")
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom = 0.2, top = 0.9)
    def buildmebarchart(i=int):
        plt.legend(country)
        p = plt.plot(dates[:i],data[:i],ch,label = name,linewidth=1)
    
    animator = ani.FuncAnimation(fig, buildmebarchart, interval = 10)
    
    plt.show()
