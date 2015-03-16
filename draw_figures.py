import matplotlib.pyplot as plt
import pickle

r_path = './result/data.pkl'

if __name__ == "__main__":
    pkl = open(r_path, 'rb')  
    data1 = pickle.load(pkl)
    data2 = pickle.load(pkl)
    data3 = pickle.load(pkl)
    data4 = pickle.load(pkl)
    data5 = pickle.load(pkl)
    data6 = pickle.load(pkl)

    lens = len(data1)
    index = range(1,lens+1)
    
    plt.plot(index, data1, 'bo-')
    plt.plot(index, data2, 'bo--')
    plt.plot(index, data3, 'ro-')
    plt.plot(index, data4, 'ro--')
    plt.plot(index, data5, 'go-')
    plt.plot(index, data6, 'go--')
    plt.show()
