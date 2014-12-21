from optparse import OptionParser
import signal
import sys
import time
import os
from static_struct import *

def signal_handler(signal, frame):
    print '\nProgram Exit'
    sys.exit(0)

def parse_options():
    signal.signal(signal.SIGINT, signal_handler)
   
    parser = OptionParser(usage = '\n    python %prog -n number_of_banks [options]', 
                          description = 'this algorithm aimed ......')
    
    parser.add_option("-n", "--num-banks", dest = "bank_number",
                            type = "int",
                            help = "The number of banks")

    parser.add_option("-i", dest = "step",
                            action = 'store',
                            type = 'int',
               help = "nodes connected every step, default is 1")
   
    parser.add_option("-m", dest = 'attack_number',
                            action = 'store',
                            type = 'int',
          help = 'Once this option is given, m banks will be give a shock as 1')

    parser.add_option("-g","--num-graph", dest = 'num_graph',
                                action = 'store',
                                type = 'int',
                                default = 1,
                                help = "how many BA networks do you want to test")
    
    parser.add_option("-t","--random-times",dest = 'random_times',
                                 action = 'store',
                                 type = 'int',
                                 default = '1',
                        help = 'in random mode, repeat times for a single network')

    parser.add_option( "-f","--figure-kind", dest = 'figure_kind',
                                 action = 'store',
                                 type = 'string',
                                 default = 'line',
                        help = 'figure types you want, can be line or points')
    
    parser.add_option( "--lamuta", dest = "lamuta",
                                type = "float",
                                action = 'store',
                                default = 0.06,
                         help = 'Banks\' initial property')

    parser.add_option("--loop", dest = "max_loop",
                               action = 'store',
                               type = 'int',
                         help = 'maximum times the loop does')

    parser.add_option("-M","--attack-mode", dest = "mode",
                                action = 'store',
                                type = 'string',
                                help = 'test, purpose or random')

    parser.add_option("-d", "--degree", dest = "degree",
                               action = "store",
                               type = "string",
                               help = "in, out, or all")

    parser.add_option("-a", "--action", dest="action",
                               action = "store",
                               default = "no",
                               help = "no, info, no+info")

    (options, args) = parser.parse_args()
   
    #print options.bank_number
    #print type(options.bank_number)

    if not options.bank_number:
      parser.error('total number of banks is not given')
    
    if not options.attack_number:
      parser.error('how many banks do you want to attack?')

    if not options.mode:
      parser.error('attack mode unknown!')
    
    print 'Total number is: %d' % (options.bank_number)
    print 'Every step is: %d' % (options.step)
    print 'Banks will be attacked: %d' % (options.attack_number)
    print 'Attack mode: %s' % (options.mode)

    return options, args

def get_c_list(n, lamuta):
    return n * [lamuta]

def another_loop(myBA, ST, m_list):
    myG = multidi_to_graph(myBA)
    add_edges(myG, 4, 12)
    
    #print get_nodes_attr(myG) 
    
    last_c = get_nodes_attr_c(myBA, 3)
    for i in range(1000):
      if i == 0:
        set_nodes_S(myBA, m_list)
      else:
        update_nodes_S(myBA,ST)
      update_nodes_status(myBA)
      update_impact_between_nodes(myBA,ST)
      #update_nodes_c(myBA, myG)
      
      this_c = get_nodes_attr_c(myBA, 3)
      if (this_c == last_c):
        #print this_c
        break
      last_c = this_c
    
    default_num = get_default_num(myBA)
    return default_num
