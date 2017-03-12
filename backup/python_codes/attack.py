import matplotlib.pyplot as plt
import main
from static_struct import *
from invoke import *
from attack_invoke import *
import gen_m_list

def do_one_attack(myBA, ST, myG, opts):
    #get needed opts
    same = int(opts.same)
    n = opts.bank_number
    m = opts.attack_number
    t = opts.random_times
    mode = opts.mode 
    alpha = opts.alpha
    kind= int(opts.kind)
    result = []
    times = []
    one_result = []
    one_time = []
    degree = opts.degree
    l_path = opts.l_path
    add = opts.add

    print '%d times attack will be executed' % (t)
    for i in range(1, t+1):
        result = []
        times = []
        print '\nThis is %dth attack' % (i) 
        print 'we will attack from 1 to %d banks\n' % (m)
        
        if same==0:
            m_list=[]
            if add==1:
                if mode == 'random':
                    m_list = gen_m_list.gen_add_list(m)
                else:
                    m_list = gen_m_list.gen_purpose_list(myBA, m)
            else:
                if mode == 'random':
                    m_list = gen_m_list.gen_random_list(m)
                else:
                    m_list = gen_m_list.gen_purpose_list(myBA, m)
            pkl = open(l_path,'a')
            pickle.dump(m_list, pkl)
        else:
            if i==1:
                pkl = open(l_path,'rb')
            m_list=pickle.load(pkl)
        
        for j in range(1, m+1):
            #print m_list
            print m_list[j-1]
            init_graphs(opts, myBA, ST, myG)
            num, time = one_loop(myBA, ST, myG, m_list[j-1], kind, alpha)
            #print 'the kind is %d' % (kind)
            print '%d %s attack in %d banks caused %d default banks' % (j,mode,n,num)
            result.append(num)
            times.append(time)
            #print result
        one_result.append(result)
        one_time.append(times)
        #print one_result
    return one_result, one_time
