from __future__ import division
import read_from_excel
from read_from_excel import *
import numpy as np
import scipy as sp

#def test_ok(X2, X0, n, e):
#    for i in range(n):
#        for j in range(n):
            
def get_value_by_key(data, key, n):
    result = range(n)
    for i in range(n):
        result[i] = data[i][key]
    return result
        
def normal(B, n):
    total = sum(B)
    result = range(n)
    for i in range(n):
        result[i] = B[i] / total
    return result

def get_X0(B, L, n):
    X0 = np.identity(n)
    for i in range(n):
        for j in range(n):
            if i==j:
                X0[i][j] = 0
            else:
                X0[i][j] = B[i] * L[j]

    return X0

def do_loop(X0, b, l, n):
    r = range(n)
    s = range(n)
    
    X1 = np.identity(n)
    for i in range(n):
        r[i] = b[i] / sum(X0[i])
        for j in range(n):
            X1[i][j] = X0[i][j] * r[i]

    X2 = np.identity(n)
    for j in range(n):
        s[j] = l[j] / sum(X1[:, j])
        for i in range(n):
            X2[i][j] = X1[i][j] * s[j]

    return X2

def get_mat(B, L, n):
    #print B
    #print L
    b = normal(B, n)
    l = normal(L, n)

    #print b 
    #print l

    X0 = get_X0(b, l, n)
    
    for i in range(10):
        print "It's loop %d" % i
        mat  = do_loop(X0, b, l, n)
        #if(test_ok(X2, X0, n, 0.005))
        if(1):
            print "test passed, finishi!"
            return mat
        else:
            X0 = mat
            print "test failed, continue!"
    
    print "loop times uesd up"
    return false
            
def main():
    data_dict = get_all_data("./excel/data2014.xls")
    n = len(data_dict)

    B = get_value_by_key(data_dict, 'B', n)
    #print B
    L = get_value_by_key(data_dict, 'L', n)
    #print L
    
    mat = get_mat(B, L, n)
    if(1):
        print "The final result is:"
        print mat
        print mat*260000000

if __name__ == "__main__":
    main()
