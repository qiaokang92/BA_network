import sys
import random
import attack_invoke
import pickle
from static_struct import *

def get_diff_list_from_kind(kind_list, k, m):
    return random.sample(kind_list[k-1], m)
    if k==0 or k>6:
        print "wrong k_list argument!"
        sys.exit(1)

def gen_add_list(m):
    m_list = []
    a = range(1,m+1)
    for i in a:
        if i==1:
            m_list.append([random.choice(a)])
            #print m_list
        else:
            #print m_list[i-2]
            b = list(set(a)-set(m_list[i-2]))
            #print b
            m_list.append([random.choice(b)] + m_list[i-2])
    return m_list

def gen_purpose_list(G, m):
    a = get_max_degree_nodes(G, m)
    #a = range(m)
    result = []
    for i in range(1, m+1):
        result.append(a[0:i])
    return result

def gen_random_list(m):
    m_list=[]
    for i in range(1,m+1):
        m_list.append(attack_invoke.get_random_list(m,i))
    return m_list

if __name__=='__main__':
    list_path=sys.argv[1]
    mm = int(sys.argv[2])
    list_kind = int(sys.argv[3])
    
    m_list = []
    if list_kind==1:
        m_list = gen_add_list(mm)
    elif list_kind==2:
        m_list = gen_random_list(mm)
    elif list_kind==3:
        m_list = gen_purpose_list(mm)
    print m_list
    pkl=open(list_path,'wb')
    pickle.dump(m_list, pkl)

