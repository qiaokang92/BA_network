from static_struct import *
from invoke import *

def self_test(opts):
    #derive needed options
    n = opts.bank_number
    n0 = opts.step
    m = opts.attack_number
    c_list = get_c_list(opts.bank_number, opts.lamuta )
    s_init_list = n * [0]

    myBA = build_myBA(n, n0)
    myBA = init_myBA(myBA, c_list, s_init_list)
    ST = build_ST(n) 
    ST = init_ST(ST)
    
    m_list = get_random_list(n, m)
    print 'These banks will be attacked: %s' % (str(m_list))
    
    print 'Test finish, default banks: %d' % (one_loop(myBA, ST, m_list))

    myBA = init_myBA(myBA, c_list, s_init_list)
    ST = init_ST(ST)
    print 'Test finish, default banks: %d' % (another_loop(myBA, ST, m_list))
    
    myBA = init_myBA(myBA, c_list, s_init_list)
    ST = init_ST(ST)
    print 'Test finish, default banks: %d' % (one_loop(myBA, ST, m_list))
    #print 'Test finish, default banks: %d' % (one_loop(myBA, ST, m_list))


