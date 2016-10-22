__author__ = 'brsch'

import matplotlib.pyplot as plt
import random
import numpy as np

default_colormap = plt.cm.Accent

def ClusteredBar(Xs, list_of_Ys, subplot_int, list_of_colors=None, list_of_labels=None):
    width = 0.0667
    num_Ys = len(list_of_Ys)

    if list_of_colors == None:
        list_of_colors = [default_colormap(float(i)/num_Ys) for i in range(1,num_Ys+1)]

    if list_of_labels == False:
        list_of_labels = [None for i in range(num_Ys)]
    elif list_of_labels == None:
        list_of_labels = ['Y_%s' % i for i in range(num_Ys)]

    ax = plt.subplot(subplot_int)

    for i in range(1, num_Ys + 1):
        Ys = list_of_Ys[i-1]
        y_color = list_of_colors[i-1]
        y_label = list_of_labels[i-1]
        plt.bar(Xs, Ys, width, color=y_color, label=y_label, align='center')
        Xs = [x + width for x in Xs]

    if list_of_labels != False:
        plt.legend(loc='lower right')

    return ax

def StackedBar(data,subplot_int,colors=None,labels=None,monochromatic=False,direction=0):

    num_Ys = len(data)-1
    num_Xs = len(data[0])

    if colors == None:
        if monochromatic == False:
            colors = [None for i in range(num_Ys)]
        else:
            if direction == 0:
                colors =  [default_colormap(float(i)/num_Ys) for i in range(1,num_Ys+1)]
            else:
                colors = [default_colormap(1-(float(i)/num_Ys)) for i in range(1,num_Ys+1)]

    if labels == False:
        labels = [None for i in range(num_Ys)]
    elif labels == None:
        labels = ['Y_%s'%i for i in range(num_Ys)]

    Xs = data[0]
    Bottom = [0 for x in range(num_Xs)]

    ax = plt.subplot(subplot_int)

    for i in range(1,num_Ys+1):
        Ys = data[i]
        y_color=colors[i-1]
        y_label=labels[i-1]
        plt.bar(Xs,Ys,bottom=Bottom,color=y_color,label=y_label,align='center')
        Bottom = [Ys[j] + Bottom[j] for j in range(len(Bottom))]

    plt.xlim(min(Xs),max(Xs))

    if labels != False:
        plt.legend(loc='lower right')
    return ax

def Lines(data,subplot_int,colors=None,labels=None,monochromatic=False,direction=0,markers=False):

    num_Ys = len(data)-1

    if colors == None:
        if monochromatic == False:
            colors = [None for i in range(num_Ys)]
        else:
            if direction == 0:
                colors =  [default_colormap(float(i)/num_Ys) for i in range(1,num_Ys+1)]
            else:
                colors = [default_colormap(1-(float(i)/num_Ys)) for i in range(1,num_Ys+1)]
    if labels == None:
        labels = ['Y_%s'%i for i in range(num_Ys)]

    Xs = data[0]
    ax = plt.subplot(subplot_int)

    for i in range(1,num_Ys+1):
        Ys = data[i]
        y_color = colors[i-1]
        y_label = labels[i-1]
        plt.plot(Xs,Ys,color=y_color,label=y_label,
                 marker='o' if markers == True else None,
                 markersize=10 if markers == True else None)
    plt.legend(loc='lower right')
    return ax

def BestFitLine(xd,yd,subplot_int,Xs_Are_Dates=False):

    if Xs_Are_Dates:
        dates_to_ints

    ax = plt.subplot(subplot_int)
    # sort the data
    reorder = sorted(range(len(xd)), key = lambda ii: xd[ii])
    xd = [xd[ii] for ii in reorder]
    yd = [yd[ii] for ii in reorder]

    # make the scatter plot
    plt.scatter(xd, yd, s=30, alpha=0.15, marker='o')

    # determine best fit line
    par = np.polyfit(xd, yd, 1, full=True)

    slope=par[0][0]
    intercept=par[0][1]
    xl = [min(xd), max(xd)]
    yl = [slope*xx + intercept  for xx in xl]

    # coefficient of determination, plot text
    variance = np.var(yd)
    residuals = np.var([(slope*xx + intercept - yy)  for xx,yy in zip(xd,yd)])
    Rsqr = np.round(1-residuals/variance, decimals=2)
    plt.text(.7*max(xd)+.3*min(xd),.9*max(yd)+.1*min(yd),'$R^2 = %0.2f$'% Rsqr, fontsize=30,color=(.5,.5,.5))

    # error bounds
    yerr = [abs(slope*xx + intercept - yy)  for xx,yy in zip(xd,yd)]
    par = np.polyfit(xd, yerr, 2, full=True)

    yerrUpper = [(xx*slope+intercept)+(par[0][0]*xx**2 + par[0][1]*xx + par[0][2]) for xx,yy in zip(xd,yd)]
    yerrLower = [(xx*slope+intercept)-(par[0][0]*xx**2 + par[0][1]*xx + par[0][2]) for xx,yy in zip(xd,yd)]

    plt.plot(xl, yl, '-', color=(.5,.5,.5))
    plt.plot(xd, yerrLower, '--', color=(.5,.5,.5))
    plt.plot(xd, yerrUpper, '--', color=(.5,.5,.5))
    return ax

"""
fig = plt.figure(1)
ax = Lines([[1,2,3],
       [4,4,4],
       [7,10,13],
       [4,16,64]],111,monochromatic=True)
fig.add_subplot(ax)
plt.show()
fig = plt.figure(0)
X = range(100)
Y = [random.random()*100 for i in range(100)]
ax = BestFitLine(X,Y,132)
plt.show()
"""