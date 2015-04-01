from static_struct import *
from invoke import *
from gen_graph import *
import sys

g_path = sys.argv[1]
m = int(sys.argv[2])
def self_test():
    myBA, ST, myG = get_graphs_from_file(g_path)
    n = myBA.number_of_nodes()
    
    c_list = n * [0.06]
    s_init_list = n * [0]
    
    init_myBA(myBA, c_list, s_init_list)
    init_ST(ST)
    init_myG(myG)

    m_list = get_random_list(n, m)
    print 'These banks will be attacked: %s' % (str(m_list))
    
    result, data = one_loop(myBA, ST, myG, m_list, 1, 0.01)
    print 'Test finish, default banks: %d' % (result)

if __name__ =='__main__':
    self_test()
