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
        #Making a list of days from when the virus started spreading, 15-2-2020(acc. to worldometer.com )

    fig = plt.figure()

    plt.ylabel("No. of People")#label for y axis 
    plt.xlabel("Dates")# label for x axis

    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom = 0.2, top = 0.9)

    def buildmebarchart(i=int):
        plt.legend(country)
        p = plt.plot(dates[:i],data[:i],ch,label = name,linewidth=1)
        # we iterate through each point to be plotted one after the other giving a animation effect 

    animator = ani.FuncAnimation(fig, buildmebarchart, interval = 10)
        # interval between each point being plotted is 10ms

    plt.show()

def plotsim(data,ch):
    dates = []
    for i in range(len(data)):
        dates.append((date((ini + timedelta(days = i)).year,(ini + timedelta(days = i)).month,(ini + timedelta(days = i)).day)))

    fig = plt.figure()

    plt.ylabel("No. of People")
    plt.xlabel("Dates")
    plt.xticks(rotation=45)

    plt.subplots_adjust(bottom = 0.2, top = 0.9)

    l = len(data)
    t = 20*1000
    i = t/l 
    # making the time interval between each point being plotted change such that any simulation user asks for takes the same amount of time
    def animation(i = int):
        p = plt.plot(dates[:1],data[:1],ch,linewidth=1)
    
    animator = ani.FuncAnimation(fig,animation,interval = i)

    plt.show()
