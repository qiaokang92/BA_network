
import networkx as nx
import sys
import os 
import signal
import time
import matplotlib.pyplot as plt
from optparse import OptionParser
from static_struct import *
#from static_vars import *


def signal_handler(signal, frame):
    print '\nProgram Exit'
    sys.exit(0)

def parse_para():
    signal.signal(signal.SIGINT, signal_handler)
   
    parser = OptionParser(usage = '\n    python %prog -n number_of_banks --manual [options]\n    python %prog -n number_of_banks -m bank_chosen_num [options]', 
                          description = 'this algorithm aimed ......')
    
    parser.add_option("-n", action = 'store',
                            dest = "BANK_NUM", 
                            help = "The number of banks")

    parser.add_option("-i", dest = "N0",
                            type = "int", 
                            default = 1,
                            action = 'store',
               help = "nodes connected every step, default is 1")
    
    parser.add_option("-m", dest = 'BANK_CHOSEN_NUM',
                            action = 'store',
          help = 'Once this option is given, m banks will be give a shock as 1')
    
    parser.add_option( "--manual", dest = 'verbose',
                                 action = 'store_true',
                                 default = False,
                        help = 'Choose banks manually')
    
    parser.add_option( "--lamuta", dest = "LAMUTA",
                               action = 'store',
                               default = 0,
                         help = 'Banks\' initial property')

    (options, args) = parser.parse_args()
    
    if not options.BANK_NUM:
      print >> sys.stderr, 'ERROR : total number is not given!\n'
      parser.print_help()
      sys.exit(1)
    else:
      n = int(options.BANK_NUM)

    if not options.N0:
      print >> sys.stderr, 'WARNING : step number is not given, set as 1'      
      n0 = 1
 
    if options.N0 > n:
      print >> sys.stderr, 'WARNING : step number too large, set as 1'
      n0 = 1   
  
    if not options.LAMUTA:
      print >> sys.stderr, 'WARNING : lamuta is not given, set as 0'

    if options.BANK_CHOSEN_NUM:
      m = int(options.BANK_CHOSEN_NUM)
      m_list = get_random_list(n,m)
    elif options.verbose:
      loop = True
      while(loop):
        m_try = raw_input('Please in put your numbers, seperate by comma:')
        m_list = eval(m_try) 
        if type(m_list) is int:
          tmp = m_list
          m_list = []
          m_list = [tmp]
        loop = False
        for i in m_list:
          if i > n :
            print >> sys.stderr, 'One or more given numbers is too large!'
            loop = True
        if len(m_list)  > n:
            print >> sys.stderr, 'number of numbers is larger than population!'
            loop = True
    else:
      parser.print_help()
      sys.exit(1)

    lamuta = int(options.LAMUTA)
    c_list  = n * [lamuta]
    S_init_list = n * [0]
    max_loop_times = range(20)

    print n
    print len(m_list)
    print m_list
    main(n, n0, m_list, c_list, S_init_list, max_loop_times)
    

def main(n, n0, m_list, c_list, S_init_list, max_loop_times):
    myBA = init_myBA(n,n0,c_list,S_init_list)
    ST = init_ST(n) 
    
    for time in max_loop_times:
      if time == 0:
        set_nodes_S(myBA,m_list)
      update_nodes_status(myBA)
      update_impact_between_nodes(myBA,ST)
      udpate_nodes_S(myBA,ST)
    
    default_num = get_default_num(myBA)
    print default_num      

if __name__ == '__main__':
    parse_para()
