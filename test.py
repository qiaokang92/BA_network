import networkx as nx
import matplotlib.pyplot as plt
from static_struct import *

# number of banks
n = 20

# second parameter of building BA network
n0 = 1

# number of nodes chosen to give a shock
m = 3

# or given banks instead of random bannks
m_list = [1,2,3,4,5,6,7]

# banks' property
c_list = [0.6] * n

# to initialize the bank's impact from others
S_init_list = [0] * n

# maximum times
max_loop_time = range(10)

def main():
    myBA = build_network(n,n0)
    
    init_edges_attr_e(myBA)
    init_nodes_LB(myBA)
    init_nodes_CS(myBA,c_list,S_init_list)
    init_nodes_status(myBA) 
     
    print myBA.edges() 
    print get_edges_attr(myBA)
    print get_nodes_attr(myBA)
    
    ST = nx.complete_graph(n, create_using = nx.MultiDiGraph())
    init_impact_between_nodes(ST)   
    
    print get_edges_attr(ST)
    
    for time in max_time:
      if time == 0:
        set_nodes_S(myBA,m_list)
      update_nodes_status(myBA)
      update_impact_between_nodes(myBA,ST)
      udpate_nodes_S(myBA,ST)
    
    print get_nodes_attr(myBA)       
    
    default_num = get_default_num(myBA)

    print default_num      





if __name__ == '__main__':
    main()
