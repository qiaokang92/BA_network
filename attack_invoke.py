import matplotlib.pyplot as plt
import main
from static_struct import *
from invoke import *

def gen_figure(data, figure_kind):
    for i in data:
      if len(i) == 0:
        draw_figure(i, figure_kind, '-')
    plt.show()

def gen_graphs(opts):
    n = opts.bank_number
    n0 = opts.step

    myBA = build_myBA(n, n0)
    ST = build_ST(n)
    myG = build_myG(myBA, n0, 12)
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

def get_average_list_1(result):
    groups = len(result)
    times = len(result[0])
    lens = len(result[0][0])
    result2 = []

    for k in range(0, groups):
        result1 = []
        for i in range(0, lens):
            total = 0
            for j in range(0,times):
                total += result[k][j][i]
            result1.append(total / times)
        result2.append(result1)
    
    return result2

def get_average_list_2(result):
    groups = len(result)
    lens = len(result[0])
    num = []

    for i in range(0,lens):
        total = 0
        for j in range(0, groups):
            total += result[j][i]
        num.append(total / groups)
    return num

def draw_figure(result, kind, line):
    groups = len(result)
    times = len(result[0])
    lens = len(result[0][0])
    
    if kind == 'single_line':
      ave1 = get_average_list_1(result)
      ave = get_average_list_2(ave1)
      index = range(1, lens+1)
      plt.plot(index, ave, line)
      #plt.show()
    
    elif kind == 'lines':
      index = range(1, lens+1)
      for i in range(0, groups):
        for j in range(0, times):
          plt.plot(index, result[i][j], line)
      #plt.show()

    elif kind == 'points':
      index = range(1, lens+1)
      for i in range(0, groups):
        for j in range(0, times):
          plt.plot(index, result[i][j], 'o', line)
      #plt.show()

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

def one_loop(myBA, ST, myG, m_list, kind):
    attack_num = len(m_list) 
    last_c = get_nodes_attr_c(myBA, 3)
    for i in range(1000):
      if i == 0:
        set_nodes_S(myBA, m_list)
      else:
        update_nodes_S(myBA,ST)
      update_nodes_status(myBA, myG)
      update_impact_between_nodes(myBA,ST)
      if kind:
        update_nodes_c(myBA, myG)
      
      this_c = get_nodes_attr_c(myBA, 3)
      if (this_c == last_c):
        print '%d attack looped %d times' % (attack_num, i)
        break
      last_c = this_c
    
    default_num = get_default_num(myBA)
    return default_num


