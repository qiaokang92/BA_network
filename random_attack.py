import networkx as nx
import sys
import os
import signal
import time
from optparse import OptionParser
from static_struct import *
import test
import global_values as gv


def do_random_attack():
    #print 'start random'
    myBA = build_myBA(gv.TOTAL_NUM, gv.N0)
    ST = build_ST(gv.TOTAL_NUM)
    #print 'build finish'

    for i in range(1,31):
      for j in range(1,11):
        gv.M = i
        gv.M_LIST = get_random_list(gv.TOTAL_NUM,gv.M)
      
        myBA = init_myBA(myBA, gv.C_LIST, gv.S_INIT_LIST)
        ST = init_ST(ST)    
        #print 'initialization finish'

        num = test.one_loop(myBA, ST)
        print '%d random attack in %d banks caused %d default banks' % (i,gv.TOTAL_NUM,num) 


if __name__ == '__main__':
    test.parse_para()
    do_random_attack()



