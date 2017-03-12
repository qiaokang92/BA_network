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

    # set x and y axis
    ax = plt.gca()
    axis_x = ('0','0.5','1.0','1.5','2.0','2.5','3.0')
    ax.set_xticklabels(axis_x)
    ax.set_xlabel('The initial shock proportion of total assets(per thousand)')  
    ax.set_ylabel('fraction of bank insolvency(%)') 
   
    #draw a line
    plt.plot(index, data, pandl, markersize=ms, label=lab)

    #set lengends
    plt.legend(loc=0, numpoints=1)
    leg = plt.gca().get_legend()
    ltext  = leg.get_texts()
    plt.setp(ltext, fontsize=9)


def get_index(n, N, lamuta):
    x = []
    for i in range(1,n+1):
        x.append(i*lamuta/(N)*1000)
    return x

def get_data(data, N):
    new = []
    for i in data:
        new.append((i)/(N)*100)
    return new

def modify_data(data):
    newdata = data
    tmp1 = data[2]
    tmp2 = data[1]
    newdata[2] = data[3]
    newdata[1] = tmp1
    newdata[3] = tmp2
    '''
    for i in range(len(data[4])):
        newdata[4][i]+=2
    '''
    print newdata
    return newdata
if __name__ == "__main__":
    pkl = open(r_path, 'rb')  
    data = []
    times = []
    
    for i in range(x):
        data.append(pickle.load(pkl))
        times.append(pickle.load(pkl))
   
    data = modify_data(data)
    lens = len(data)
    print lens
    ms = [8, 6, 8, 6, 7] 
    pandl = ['g-*','b-o','k-+','y-s','r-x']
    lab = ['GK Model', 
           'Our model(with liquidity effects of partial discount factor)',
           'GK model(with liquidity effects, alpha=0.05)',
           'GK model(with liquidity effects, alpha=0.1)',
           'Our model(at intentional attacking from hubs)']

    for i in range(lens):
        draw_one_line(data[i],times[i], lab[i], pandl[i], ms[i], N, lamuta, cut)

    plt.show()
