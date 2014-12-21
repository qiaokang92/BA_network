import networkx as nx
import sys
import os 
import signal
import time
from static_struct import *
from attack import *
from test import *

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
    #get needed options:
    num_graph = opts.num_graph
    figure_kind = opts.figure_kind
    m = opts.attack_number
    mode = opts.mode

    print ('\n %d graphs will be tested') % (num_graph)

    for i in range(1, num_graph + 1):
        print '\nThe %dth graph will be established' % (i)
        myBA, ST, myG = gen_graphs(opts)
        if opts.action == 'no':
            all_result1.append(do_one_attack(myBA, ST, myG, opts, False))
        elif opts.action =='info':
            all_result1.append(do_one_attack(myBA, ST, myG, opts, True))
        elif opts.action == 'no+info':
            all_result1.append(do_one_attack(myBA, ST, myG, opts, False))
            all_result2.append(do_one_attack(myBA, ST, myG, opts, True))

    data = [all_result1, all_result2]
    #save_data(data)
    gen_figure(data, figure_kind)

if __name__ == '__main__':
    opts, args = parse_options()
    enter_attack(opts, args)
