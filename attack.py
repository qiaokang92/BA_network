import matplotlib.pyplot as plt
import main
from static_struct import *
from invoke import *
from attack_invoke import *
import gen_m_list
from gen_real_graph import *

def do_one_attack(myBA, ST, myG, opts, kind_list):
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
    k = opts.k
    
    beita = opts.beita
    if beita > 0:
        beita_list = [beita * 0.01] * 100
    else:
        beita_list=[0]*100
        for i in range(0,100):
            beita_list[i] = (i+1)*0.01
    
    #print '%d times attack will be executed' % (t)
    for i in range(1, t+1):
        #result = []
        #times = []
        #print '\nThis is %dth attack' % (i) 
        #print 'we will try to attack %d banks\n' % (m)
        
        '''
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
        '''

        if mode == 'random':
            m_list = gen_m_list.get_diff_list_from_kind(kind_list, k, m)
            #print 'Will attack this banks:'
            #print 'ReIniting Graphs'
            init_real_graphs(opts, myBA, ST, myG)
            #print 'beita is %f' % beita
            num, time = one_loop(myBA, ST, myG, m_list, kind, alpha, beita)
            print m_list
            print 'It is the %d attack: %d defaults ' % (i, num)
            print 
            #print 'random %d attack in kind-%d caused %d default banks' % (m, k, num)
            one_result.append(num)
            #time.append(time)
        elif mode == 'kind_all':
            m_list = kind_list[k - 1]
            #print m_list
            print  '  '
            print 'beita is %f' % beita_list[i-1]
            init_real_graphs(opts, myBA, ST, myG)
            #print 'reinit finish!'
            num, time = one_loop(myBA, ST, myG, m_list, kind, alpha, beita_list[i-1])
            print 'ALL attack in kind %d caused %d default banks, loop times: %d' % (k, num, time+1)
            one_result.append(num)
            #time.append(time)

        #print one_result


        '''
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
        '''
        #print result
    #one_result.append(result)
    #one_time.append(times)
        #print one_result
    return one_result, one_time   
    #return one_result, one_time
