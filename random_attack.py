import matplotlib.pyplot as plt
import sys
import main
from static_struct import *


def do_random_attack(n, n0, m, c_list, s_init_list):
    all_result = []
    
    print '\n20 graphs will be tested'
    for i in range(1,21):
        print '\nThe %dth graph will be established' % (i)
        all_result.append(do_one_random_attack(n, n0, m, c_list, s_init_list))
    print all_result
    
    fd = open('./result/random', 'w')
    fd.write(str(all_result))
    
    ave1 = get_average_list_1(all_result)
    print ave1
    ave2 = get_average_list_2(ave1)
    print ave2

    index = range(1, m+1)
    draw(index, ave2)
    return all_result

def do_one_random_attack(n, n0, m, c_list, s_init_list):
    result = []
    one_result = []

    myBA = build_myBA(n, n0)
    ST = build_ST(n)

    print '\nNew graph established, number of nodes: %d' % (n)
    print 'Average degree: %d' % (get_average_degree(myBA))

    print '10 times attack will be executed'
    for i in range(1, 11):
        result = []
        print '\nThis is %dth attack' % (i) 
        print 'we will attack from 1 to %d banks' % (m)
        for j in range(1, m+1):
            m_list = get_random_list(n, j)
            #print m_list
            #print '%d banks will be randomly attacked' % (j)

            myBA = init_myBA(myBA, c_list, s_init_list)
            ST = init_ST(ST)

            num = main.one_loop(myBA, ST, m_list)
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

def draw(index, ave):
    plt.plot(index, ave)
    plt.show()

if  __name__ == '__main__':
    test.parse_para()
    do_random_attack()



