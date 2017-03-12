import networkx as nx
import sys
import os
import signal
import time
from static_struct import *
from attack import *
from test import *
import pickle

def get_graphs_from_file(path):
    g_file = open(path, 'rb')
    data = pickle.load(g_file)
    g_file.close()
    return data[0], data[1], data[2]

if __name__ == "__main__":
    opts, args = parse_options()
    myBA, ST, myG = gen_graphs(opts)
    
    data = [myBA, ST, myG]

    g_path = opts.graph_path
    output = open(g_path, 'wb')
    pickle.dump(data, output)
    output.close()

    
