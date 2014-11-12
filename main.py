import networkx as nx
import sys
import os 
import signal
import time
from optparse import OptionParser
from static_struct import *
from  purpose_attack import *

def signal_handler(signal, frame):
    print '\nProgram Exit'
    sys.exit(0)

def parse_para():
    signal.signal(signal.SIGINT, signal_handler)
   
    parser = OptionParser(usage = '\n    python %prog -n number_of_banks [options]', 
                          description = 'this algorithm aimed ......')
    
    parser.add_option("-n", action = 'store',
                            dest = "N", 
                            help = "The number of banks")

    parser.add_option("-i", dest = "N0",
                            action = 'store',
               help = "nodes connected every step, default is 1")
   
    parser.add_option("-m", dest = 'M',
                            action = 'store',
          help = 'Once this option is given, m banks will be give a shock as 1')
    
    parser.add_option( "--manual", dest = 'verbose',
                                 action = 'store_true',
                                 default = False,
                        help = 'Choose banks manually')
    
    parser.add_option( "--lamuta", dest = "LAMUTA",
                               action = 'store',
                         help = 'Banks\' initial property')

    parser.add_option("--loop", dest = "MAX_LOOP",
                               action = 'store',
                               type = 'int',
                         help = 'maximum times the loop does')
    parser.add_option("--mode", dest = "MODE",
                                action = 'store',
                                type = 'string',
                                help = 't, p or r')
    parser.add_option("--degree", dest = "DEGREE",
                               action = "store",
                               type = "string",
                               help = "in, out, or all")

    (options, args) = parser.parse_args()
    
    if not options.N:
      parser.error('total number is not given')
    else:
      n  = int(options.N)
    
    if options.DEGREE:
      degree = options.DEGREE
    else:
      degree = ''

    if options.MODE:
      mode = options.MODE

    if options.M:
      m = int(options.M)

    if not options.N0:
      print >> sys.stderr, 'WARNING : step number is not given, set as 1'      
      n0 = 1
    else:
      n0 = int(options.N0)
 
    if not options.LAMUTA:
      print >> sys.stderr, 'WARNING : lamuta is not given, set as 0.6'
      lamuta = 0.6
 
    c_list  = n * [lamuta]
    s_init_list = n * [0]

    print 'Total number is: %d' % (n)
    print 'Every step is: %d' % (n0)
    print 'Banks will be attacked: %d' % (m)
    print 'Attack mode: %s' % (mode)

    do_attack(n, n0, m, c_list, s_init_list, mode, degree)
    
def do_attack(n, n0, m, c_list, s_init_list, mode, degree):
    if mode == 't':
        print 'Mode: test'
        self_test(n, n0, m, c_list, s_init_list)
    elif mode == 'r':
        print 'Mode: random attack'
        do_random_attack(n, n0, m, c_list, s_init_list)
    elif mode == 'p':
        print 'Mode: purpose attack'
        do_purpose_attack(n, n0, m, c_list, s_init_list, degree)

def self_test(n, n0, m, c_list, s_init_list):
    myBA = build_myBA(n, n0)
    myBA = init_myBA(myBA, c_list, s_init_list)
    ST = build_ST(n) 
    ST = init_ST(ST)
    
    m_list = get_random_list(n, m)
    print 'These banks will be attacked: %s' % (str(m_list))
    print 'Test finish, default banks: %d' % (one_loop(myBA, ST, m_list))

def one_loop(myBA, ST, m_list):
    last_c = get_nodes_attr_c(myBA)
    
    for i in range(1000):
      if i == 0:
        set_nodes_S(myBA, m_list)
      update_nodes_status(myBA)
      #print 'update status finish'
      update_impact_between_nodes(myBA,ST)
      #print 'update s finish'
      udpate_nodes_S(myBA,ST)
      #print 'update S finish'
      
      this_c = get_nodes_attr_c(myBA)
      if (this_c == last_c):
        break
      last_c = this_c
      #print 'test c finish'
      
    default_num = get_default_num(myBA)
    return default_num

if __name__ == '__main__':
    parse_para()
