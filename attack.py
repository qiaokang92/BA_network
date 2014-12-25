import matplotlib.pyplot as plt
import main
from static_struct import *
from invoke import *
from attack_invoke import *

def do_one_attack(myBA, ST, myG, opts, kind):
    #get needed opts
    n = opts.bank_number
    m = opts.attack_number
    t = opts.random_times
    mode = opts.mode 
    result = []
    one_result = []
    degree = opts.degree

    print '%d times attack will be executed' % (t)
    for i in range(1, t+1):
        result = []
        print '\nThis is %dth attack' % (i) 
        print 'we will attack from 1 to %d banks\n' % (m)
        for j in range(1, m+1):
            if mode == 'random':
                m_list = get_random_list(n, j)
            elif mode == 'purpose':
                m_list = get_purpose_list(myBA, j, degree) 
            print m_list
            init_graphs(opts, myBA, ST, myG)
            num = one_loop(myBA, ST, myG, m_list, kind)
            print '%d %s attack in %d banks caused %d default banks' % (j,mode,n,num)
            result.append(num)
            #print result
        one_result.append(result)
        #print one_result
    return one_result
