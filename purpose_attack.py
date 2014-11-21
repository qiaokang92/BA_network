import matplotlib.pyplot as plt
import cPickle
import main
from static_struct import *
import sys

def init_purpose_list(G, m, degree):
    n = G.number_of_nodes()
    if degree == 'all':
      #return get_random_list(n,m)
      return get_max_degree_nodes(G, m)
    elif degree == 'in':
      return get_max_indegree_nodes(G, m)
    elif degree == 'out':
      return get_max_outdegree_nodes(G, m)

def do_one_purpose_attack(n,n0,m,c_list,s_init_list,degree):
    result = []
    
    myBA = build_myBA(n, n0)
    ST = build_ST(n)
    #print get_nodes_in_degree(myBA)
    print 'Average degree: %d' % (get_average_degree(myBA))

    for i in range(1, m+1):
      m_list = init_purpose_list(myBA, i, degree)
      print m_list
      
      myBA = init_myBA(myBA, c_list, s_init_list)
      ST = init_ST(ST)
      
      num = main.one_loop(myBA, ST, m_list)
      result.append(num)
      print '%d purpose attack in %d banks caused %d default banks' % (i,n, num)
    return result

def do_purpose_attack(n, n0, m, c_list, s_init_list, degree):
    all_result = []
    for i in range(1,21):
      all_result.append(do_one_purpose_attack(n, n0, m, c_list, s_init_list, degree))
    print all_result
    
    #fd = open('./purpose_result', 'w')
    #fd.write(str(all_result))
    
    ave = get_average_list(all_result)
    print ave
    index = range(1, m + 1)
    draw(index, ave)
     
    fd = open('./test', 'w')
    fd.write(str(all_result))
    return all_result

def get_average_list(result):
    groups = len(result)
    lens = len(result[0])
    num = []

    for i in range(0, lens):
      total = 0
      for j in range(0, groups):
         total += result[j][i]
      num.append(total / groups)
    return num

def draw(index, ave):
    plt.plot(index, ave)
    plt.show()
