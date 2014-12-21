import matplotlib.pyplot as plt
import main
from static_struct import *
from invoke import *

def do_random_attack(opts):
    data = []
    all_result1 = []
    all_result2 = []
    #get needed options:
    num_graph = opts.num_graph
    figure_kind = opts.figure_kind
    m = opts.attack_number

    print ('\n %d graphs will be tested') % (num_graph)
    for i in range(1, num_graph + 1):
        print '\nThe %dth graph will be established' % (i)
        myBA, ST, myG = gen_graphs(opts)
        if opts.action == 'no':
            all_result1.append(do_one_random_attack(myBA, ST, myG, opts, False))
        elif opts.action =='info':
            all_result1.append(do_one_random_attack(myBA, ST, myG, opts, True))
        elif opts.action == 'no+info':
            all_result1.append(do_one_random_attack(myBA, ST, myG, opts, False))
            all_result2.append(do_one_random_attack(myBA, ST, myG, opts, True))
        #all_result2
    #print all_result
    data = [all_result1, all_result2]
    parse_figure(data, figure_kind)

def parse_figure(data, figure_kind):
    if len(data[1]) == 0:
        draw_figure(data[0], figure_kind, '-')
    else:
        draw_figure(data[0], figure_kind, '-')
        draw_figure(data[1], figure_kind, '--')
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

def do_one_random_attack(myBA, ST, myG, opts, kind):
    #get needed opts
    n = opts.bank_number
    m = opts.attack_number
    t = opts.random_times
    
    result = []
    one_result = []

    print '%d times attack will be executed' % (t)
    for i in range(1, t+1):
        result = []
        print '\nThis is %dth attack' % (i) 
        print 'we will attack from 1 to %d banks\n' % (m)
        for j in range(1, m+1):
            m_list = get_random_list(n, j)
            init_graphs(opts, myBA, ST, myG)
            num = one_loop(myBA, ST, myG, m_list, kind)
            print '%d random attack in %d banks caused %d default banks' % (j,n,num)
            result.append(num)
            #print result
        one_result.append(result)
        #print one_result
    return one_result


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
def get_simple_result(result):
    groups = len(result)
    times = len(result[0])
    lens = len(result[0][0])
    simple = []
    for i in range(0, groups):
        for j in range(0, times):
            simple += result[i][j]
    return simple

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
    '''
    simple = get_simple_result(result)
    index = range(1, lens+1) * groups * times
    plt.plot(index, simple, 'o')
    plt.show()
    #print 'should draw a points figure'
    '''

if  __name__ == '__main__':
    test.parse_para()
    do_random_attack()



