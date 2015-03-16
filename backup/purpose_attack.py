import matplotlib.pyplot as plt
import sys
import cPickle
import main
from invoke import *
from static_struct import *
from purpose_invoke import *

def do_one_purpose_attack(opts):
    result = []
    times = []

    n = opts.bank_number
    n0 = opts.step
    m = opts.attack_number
    c_list = get_c_list(opts.bank_number, opts.lamuta )
    s_init_list = n * [0]
    degree = opts.degree
        
    myBA = build_myBA(n, n0)
    ST = build_ST(n)
    #print get_nodes_in_degree(myBA)
    print '\nAverage degree: %d\n' % (get_average_degree(myBA))

    for i in range(1, m+1):
      m_list = init_purpose_list(myBA, i, degree)
      print m_list
      
      myBA = init_myBA(myBA, c_list, s_init_list)
      ST = init_ST(ST)
      
      num , time = one_loop(myBA, ST, m_list)
      result.append(num)
      times.append(time)
      print '%d purpose attack in %d banks caused %d default banks' % (i,n, num)
      print 'looped %d times' % (time)
    return result, times

def do_purpose_attack(opts):
    all_result = []
    all_times = []
    num_graph = opts.num_graph
    figure_kind = opts.figure_kind
    m = opts.attack_number

    print '\n%d graphs will be established in total' % (num_graph)
    for i in range(1,num_graph + 1):
      print '\n%dst graph established' % (i)
      r = do_one_purpose_attack(opts)
      t = do_one_purpose_attack(opts)
      all_result.append(r)
      all_result.append(t)
    print all_result
   
    draw_figure(all_result, figure_kind)
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

def draw_figure(result, kind):
    groups = len(result)
    lens = len(result[0])
    if kind == 'single_line':
      ave = get_average_list(result)
      index = range(1, lens+1)
      plt.plot(index, ave)
      plt.show()
    elif kind == 'points':
      index = range(1, lens+1)
      for i in range(0, groups):
        plt.plot(index, result[i], 'o')
      plt.show()
      '''
      simple = get_simple_result(result)
      index = range(1, lens+1) * groups
      plt.plot(index, simple, 'o')
      plt.show()
      '''
    elif kind == 'lines':
      index = range(1, lens+1)
      for i in range(0, groups):
        plt.plot(index, result[i])
      plt.show()

    else:
      print 'error: wrong figure kind'
      sys.exit(2)

def get_simple_result(result):
    groups = len(result)
    lens = len(result[0])
    simple = []
    for i in range(0, groups):
      simple += result[i]
    return simple


