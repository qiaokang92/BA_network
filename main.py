import networkx as nx
import sys
import os 
import signal
import time
from static_struct import *
from attack import *
from test import *
from gen_graph import *

def enter_attack(opts, args):
    do_attack(opts)
    '''
    if opts.mode == 'test':
        #print 'Mode: test'
        self_test(opts)
    elif opts.mode == 'purpose':
        #print 'Mode: purpose attack'
        do_attack(opts)
    elif opts.mode == 'random':
        #print 'Mode: random attack'
        do_attack(opts)
    else:
       print 'error: wrong mode type!'
       sys.exit(1)
    '''

def do_attack(opts):    
    data = []
    all_result = []
    all_times = []
    #get needed options:
    num_graph = opts.num_graph
    figure_kind = opts.figure_kind
    m = opts.attack_number
    mode = opts.mode
    g_path = opts.graph_path
    r_path = opts.data_path
    #t_path = opts.txt_path

    #print ('\n %d graphs will be tested') % (num_graph)

    for i in range(1, num_graph + 1):
        #print '\nThe %dth graph will be established' % (i)
        myBA, ST, myG, kind_list = get_graphs_from_file(g_path)
        
        r,t = do_one_attack(myBA, ST, myG, opts, kind_list)
        all_result.append(r)
        #all_times.append(t)
        
    #all_data = [all_result, all_times]
    #print all_result
    
    save_data(r_path, all_result)
    
    #write_data_2_txt(t_path, all_data)
    #gen_figure(data, figure_kind)

if __name__ == '__main__':
    opts, args = parse_options()
    enter_attack(opts, args)
