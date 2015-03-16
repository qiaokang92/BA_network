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

def do_attack(opts):
    data = []
    all_result1 = []
    all_result2 = []
    all_times1 = []
    all_times2 = []
    #get needed options:
    num_graph = opts.num_graph
    figure_kind = opts.figure_kind
    m = opts.attack_number
    mode = opts.mode
    path = opts.data_path
    g_path = './result/graphs.pkl'
    r_path = './result/data.pkl'
    t_path = opts.txt_path

    print ('\n %d graphs will be tested') % (num_graph)

    for i in range(1, num_graph + 1):
        print '\nThe %dth graph will be established' % (i)
        
        #myBA, ST, myG = gen_graphs(opts)
        myBA, ST, myG = get_graphs_from_file(g_path)

        if opts.action == 'no':
            all_result1.append(do_one_attack(myBA, ST, myG, opts, False))
        elif opts.action =='info':
            all_result1.append(do_one_attack(myBA, ST, myG, opts, True))
        elif opts.action == 'no+info':
            print '\nattack without information level'
            r1,t1 = do_one_attack(myBA, ST, myG, opts, False)
            all_result1.append(r1)
            all_times1.append(t1)
            print '\nattack with information level'
            r2,t2 = do_one_attack(myBA, ST, myG, opts, True)
            all_result2.append(r2)
            all_times2.append(t2)
        else:
            print 'error action type'
            sys.exit(3)
    data = [all_result1, all_result2]
    times = [all_times1, all_times2]
    all_data = [data, times]
    #print all_data 
    save_data(r_path, all_data)
    
    write_data_2_txt(t_path, all_data)

    #gen_figure(data, figure_kind)

if __name__ == '__main__':
    opts, args = parse_options()
    enter_attack(opts, args)
