from __future__ import division
from pylab import *
import pickle
import matplotlib.pyplot as plt
import sys

r_path = sys.argv[1]
x = int(sys.argv[2])
lamuta = float(sys.argv[3])
N = int(sys.argv[4])
cut = int(sys.argv[5])

def draw_one_line(data, times, lab, pandl, ms, N, lamuta, cut):
    data = data[0:cut]
    lens = len(data)
    index = get_index(lens, N, lamuta)
    data = get_data(data, N)
    print index

    # set x and y axis
    ax = plt.gca()
    #axis_x = ('0','0.5','1.0','1.5','2.0','2.5','3.0')
    #axis_x = ('0','100','200','300','400','500')
    #ax.set_xticklabels(axis_x)
    #axis_y = ('0','10','20','30','40','50','60','70','80','90','100')
    #ax.set_yticklabels(axis_y)
    
    ylim(0,100)
    
    ax.set_xlabel('network size')  
    ax.set_ylabel('fraction of bank insolvency(%)') 
   
    #draw a line
    plt.plot(index, data, pandl, markersize=ms, label=lab)

    #set lengends
    plt.legend(loc=0, numpoints=1)
    leg = plt.gca().get_legend()
    ltext  = leg.get_texts()
    plt.setp(ltext, fontsize=12)


def get_index(n, N, lamuta):
    x = []
    for i in range(1,n+1):
        x.append(i*10*5/3)
    return x

def get_data(data, N):
    new = []
    for i in data:
        new.append((i)/(N)*100)
    return new

def modify_data(data):
    newdata = [1,2,3,4,5,6]
    newdata[0] = data[0]
    newdata[1] = data[2]
    newdata[2] = data[4]
    newdata[3] = data[6]
    newdata[4] = data[8]
    newdata[5] = data[10]
    return newdata
def modify_data2(data):
    newdata = [1,2,3,4,5,6]
    newdata[0] = data[1]
    newdata[1] = data[3]
    newdata[2] = data[5]
    newdata[3] = data[7]
    newdata[4] = data[9]
    newdata[5] = data[11]
    return newdata
if __name__ == "__main__":
    pkl = open(r_path, 'rb')  
    data = []
    times = []
    
    for i in range(x):
        data.append(pickle.load(pkl))
        times.append(pickle.load(pkl))
   
    #data = modify_data(data)
    data = modify_data2(data)
    lens = len(data) 
    print lens
    ms = [7, 7, 7, 7, 7, 7]
    ms.reverse()
    #pandl = ['g-*','b-o','k-+','y-s','r-x', 'm-D']
    pandl = ['g-x','b-o','k-<','y->','r-^', 'm-v']
    lab1 = ['m=2, C=0.5',
           'm=2, C=0.6', 
           'm=3, C=0.68',
           'm=3, C=0.72',
           'm=4, C=0.76',
           'm=4, C=0.79']
    lab2 = ['m=4, Z=9',
           'm=4, Z=8', 
           'm=3, Z=7',
           'm=3, Z=6',
           'm=2, Z=5',
           'm=2, Z=4']
    temp = range(lens)
    #pandl.reverse()
    #lab.reverse()
    #temp.reverse()
    for i in temp:
        draw_one_line(data[i],times[i], lab1[i], pandl[i], ms[i], N, lamuta, cut)

    plt.show()
