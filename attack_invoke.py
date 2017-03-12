import matplotlib.pyplot as plt
import main
from static_struct import *

def get_c_list(n,lamuta):
    return n * [lamuta]

def gen_graphs(opts):
    n = opts.bank_number
    n0 = opts.step

    myBA = build_myBA(n, n0)
    ST = build_ST(n)
    myG = build_myG(myBA, n0, 25)
    print '\nNew graph established, number of nodes: %d' % (n)
    print 'Average degree: %d' % (get_average_degree(myBA))
    return myBA, ST, myG

def init_graphs(opts, myBA, ST, myG):
    n = opts.bank_number
    c_list = get_c_list(opts.bank_number, opts.lamuta )
    s_init_list = n * [0]
    
    init_myBA(myBA, c_list, s_init_list)
    init_ST(ST)
    init_myG(myG)

def get_purpose_list(G, m, degree):
    n = G.number_of_nodes()
    if degree == 'all':
      #return get_random_list(n,m)
      return get_max_degree_nodes(G, m)
    elif degree == 'in':
      return get_max_indegree_nodes(G, m)
    elif degree == 'out':
      return get_max_outdegree_nodes(G, m)
    else:
      print 'error: wrong degree type!'
      sys.exit(2)

def get_random_list(n,m):
    n_list = range(0,n)
    m_list =  random.sample(n_list,m)
    return m_list

def one_loop(myBA, ST, myG, m_list, kind, alpha, beita):
    attack_num = len(m_list) 
    last_c = get_nodes_attr_c(myBA, 0)
    jumpout = 0
    #print last_c
    for i in range(100):
      #print '\nthis is loop %d\n' % (i)
      if i == 0:
        set_nodes_S(myBA, m_list, beita)
      else:
        update_nodes_S(myBA,ST)

      #print 'Will calculate s for next generation'      
      update_impact_between_nodes2(myBA,ST)
      
      #print 'Will update status'
      update_nodes_status(myBA, myG)

      #print 'Enter information level'
      update_nodes_c2(myBA, myG, alpha)

      #print 'Will get c'
      this_c = get_nodes_attr_c(myBA, 0)

      #print '%d default in this loop' % get_default_num(myBA)

      if(jumpout == 1):
        jumpout = 0
        break

      if (this_c == last_c):
        #print this_c
        #print last_c
        #print '\nC equals, %d attack looped %d times' % (attack_num, i)
        jumpout = 1
        #break

      last_c = this_c
    
    default_num = get_default_num(myBA)
    return default_num , i


