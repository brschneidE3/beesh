__author__ = 'brsch'

import matplotlib.pyplot as plt
default_colormap = plt.cm.winter

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

def Lines(data,subplot_int,colors=None,labels=None,monochromatic=False,direction=0):

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
        plt.plot(Xs,Ys,color=y_color,label=y_label)
    plt.legend(loc='lower right')
    return ax

"""
fig = plt.figure(1)
ax = Lines([[1,2,3],
       [4,4,4],
       [7,10,13],
       [4,16,64]],111,monochromatic=True)
fig.add_subplot(ax)
plt.show()
"""