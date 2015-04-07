from __future__ import division
import pickle
import matplotlib.pyplot as plt
import sys

r_path = sys.argv[1]
x = int(sys.argv[2])

def draw_one_line(data, times, line, point):
    lens = len(data)
    index = range(1,lens+1)

    plt.plot(index, data, line)
    for i in range(lens):
        plt.plot(index[i], data[i], point, alpha = times[i]/(max(times)))
        #print times[i]/(max(times))

if __name__ == "__main__":
    pkl = open(r_path, 'rb')  
    data = []
    times = []
    
    #for i in range(6):
    for i in range(x):
        data.append(pickle.load(pkl))
        times.append(pickle.load(pkl))
    
    lens = len(data)
    
    line = ['g-','g--','b-','b--','k-','k--','r-','r--','y-','y--','c-','c--','m-','m--','g-','g--']
    shape = ['rs', 'rs'] * 8

    for i in range(lens):
        draw_one_line(data[i],times[i], line[i], shape[i])

    plt.show()
