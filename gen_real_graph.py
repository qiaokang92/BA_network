import pickle
from static_struct import *
import networkx as nx
import sys
import os 
import signal
import time
from attack import *
from test import *
from gen_graph import *
#Global Variables
#n = 170 # number of real banks
#n0 = 1 # the step of BA network
#d = 25 # the aim degree of myG

def create_real_myBA_myG(opts):
    n = opts.bank_number

    #mat1 = get_mat(opts.chaijie_path)
    #mat2 = get_mat(opts.gailv_path)
    #name_list = get_all_names(opts.chaijie_path)
    #kind_list = get_kind_list(opts.init_data_path)

    myBA = create_real_myBA(opts.init_data_path, opts.chaijie_path, n)
    myG = create_real_myG(myBA, opts.gailv_path)

    return myBA, myG   #(opts.init_data_path, opts.chaijie_path)

#before a second attack, reinit is needed
def init_real_graphs(opts, myBA, ST, myG):
    init_real_myBA(myBA, opts.init_data_path, opts.chaijie_path)
    init_real_myG(myG)
    init_real_ST(ST)


def init_all(opts):
    print 'Creating myBA and myG .....'
    myBA, myG = create_real_myBA_myG(opts)
    print 'myBA and myG created'
    #ST = build_ST(len(names))

    print 'Creating ST .....'
    ST = create_real_ST(opts.bank_number)
    print 'ST created, the nodes are:'
    print ST.nodes()

    '''
    print kind_list[0]
    print kind_list[1]
    print kind_list[2]
    '''
   
    #print get_average_degree(myBA)
    #print get_average_degree(myG)
    
    return myBA, ST, myG

if __name__ == '__main__':
    opts, args = parse_options()

    myBA ,ST, myG = init_all(opts)

    print "Init finish, myBA's average degree is %d" % get_average_degree(myBA)
    print "the average degree of myG is %d" % get_average_degree(myG)

    kind_list = get_kind_list(opts.init_data_path)
    print "Kind list:"
    print kind_list

    data = [myBA, ST, myG, kind_list]

    g_path = opts.graph_path
    print 'Graph Data saved to file %s' % g_path

    output = open(g_path, 'wb')
    pickle.dump(data, output)
    output.close()





