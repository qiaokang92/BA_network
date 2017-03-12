'''
This file includes some functions for 2 graphs.
The first graph G is a graph of banks, the second one includes the strike between banks.
 
Author: Kang Qiao, BUAA
Finsh Date: Oct, 25th, 2014
'''

from __future__ import division
import random
import networkx as nx
from networkx.generators.classic import empty_graph, path_graph, complete_graph
import math
import itertools
import sys

'''
build a BA network, with n nodes and each step connet m nodes
this network is directed and have multiple edges
modified from barabasi_albert_graph() in networkx.random_graphs module
'''

def build_network(n,m):
    #return nx.random_graphs.my_BA_graph(n,m)
    return local_my_BA_graph(n,m)

def local_my_BA_graph(n,m,seed=None):
    if m < 1 or  m >=n:
        raise nx.NetworkXError(\
              "Barabasi-Albert network must have m>=1 and m<n, m=%d,n=%d"%(m,n))
    if seed is not None:
        random.seed(seed)

    # Add m initial nodes (m0 in barabasi-speak)
    G=empty_graph(m,create_using=nx.MultiDiGraph())
    G.name="my BA graph, directed and muliple(%s,%s)"%(n,m)
    # Target nodes for new edges
    targets=list(range(m))
    # List of existing nodes, with nodes repeated once for each adjacent edge
    repeated_nodes=[]

    # make G a full graph
    for i in targets:
        for j in targets:
            if (i != j) and (not (i,j) in G.edges()):
                G.add_edge(i,j)
                repeated_nodes.append(i)
                repeated_nodes.append(j)
    
    # Start adding the other n-m nodes. The first node is m.
    source=m
    counter=0
    while source<n:
        # Add edges to m nodes from the source.
        targets = [i for i in targets]
        for i in range(0, m): 
            if counter % 3 == 0:
                G.add_edge(source, targets[i])
                repeated_nodes.append(targets[i])
                repeated_nodes.append(source)
            elif counter % 3 == 1:
                G.add_edge(targets[i], source)
                repeated_nodes.append(targets[i])
                repeated_nodes.append(source)
            else:
                G.add_edge(source, targets[i])
                G.add_edge(targets[i], source)
                repeated_nodes.extend([targets[i]]*2)
                repeated_nodes.extend([source]*2)
            counter += 1
        '''
        if counter % 3 == 0:
          G.add_edges_from(zip([source]*m,targets))
        elif counter % 3 == 1:
          G.add_edges_from(zip(targets,[source]*m))
        else:
          G.add_edges_from(zip(targets,[source]*m))
          G.add_edges_from(zip([source]*m,targets))
        '''
        # Add one node to the list for each new edge just created.
        #repeated_nodes.extend(targets)
        # And the new node "source" has m edges to add to the list.
        #repeated_nodes.extend([source]*m)
        # Now choose m unique nodes from the existing nodes
        # Pick uniformly from repeated_nodes (preferential attachement)
        targets = nx.random_graphs._random_subset(repeated_nodes,m)
        source += 1
    #print '1111'
    #print G.nodes()
    #print G.number_of_nodes()
    return G


# return attributes of every edges in G
def get_edges_attr(G):
    result = []
    for i in G.edges():
      start = i[0]
      to = i[1]
      show = G[start][to][0]
      show['edge'] = i
      result.append(show)
    return result

# return attributes of edge in G
def get_edge_attr(G,edge):
    start = edge[0]
    end = edge[1]
    attr = G[start][end][0]
    return attr

# return attirbutes of every nodes in G
def get_nodes_attr(G):
    result = []
    for i in G.nodes():
      show = G.node[i]
      show['node'] = i
      result.append(show)
    return result

def get_nodes_attr_c(G, precise):
    result = []
    for i in G.nodes():
      show = G.node[i]
      result.append(round(show['c'], precise))
    return result

# init the 'e' value of all edges in G 
def init_edges_attr_e(G):
    for i in G.edges():
      first = i[0]
      to = i[1]
      to_in = G.in_degree(to)
      if (to_in): 
        G.edge[first][to][0]['e'] = 0.2 / to_in 
        #print i
        #print first_in
        #print G.edge[first][to][0]   

# init the 'L' and 'B' value of all nodes in G
def init_nodes_LB(G):
    for i in G.nodes():
      result = 0
      result2 = 0
      for j in G.edges():
        if i == j[0]:
          result += get_edge_attr(G,j)['e']
        if i == j[1]:
          result2 += get_edge_attr(G,j)['e']
      G.node[i]['L'] = 0.2
      G.node[i]['B'] = result

#  init the 'c' and 'S' value of all nodes in G
#  receive 2 lists, each has n elements, like [0.6, 0.7, ...]
def init_nodes_CS(G,c,s):
    for i in G.nodes():
      G.node[i]['c'] = c[i]
      #print i 
      G.node[i]['S'] = s[i]
      #print i

# init the 'statue' value as 'Stable' of all nodes in G
def init_nodes_status(G):
    for i in G.nodes():
      G.node[i]['status'] = 'Stable'

# init the 'shock' value as zero of all edges in ST
def init_impact_between_nodes(ST):
    for i in ST.edges():
      start = i[0]
      to = i[1]
      ST[start][to][0]['shock'] = 0

# update the status and the 'c' value of every node in G
# by the change of 'S' value
def update_nodes_status(G, g):
    for i in G.nodes():
      c = G.node[i]['c']
      S = G.node[i]['S'] 
      if c > S:
        G.node[i]['c'] -= S
        G.node[i]['status'] = 'Stable'
      elif (c != 0) & (c <= S):
        G.node[i]['c'] = 0
        G.node[i]['status'] = 'Default'
        for j in g.node[i]['neibor']:
            g.node[j]['ndn'] += 1

def update_nodes_c4(BA,g,alpha):
    for i in g.nodes():
        old_rho = BA.node[i]['rho']
        BA.node[i]['rho'] = get_node_rho2(BA)
        rho = BA.node[i]['rho']

        old_ea = BA.node[i]['EA']
        BA.node[i]['EA'] = BA.node[i]['EA'] * math.exp(-0.05 * rho)
        ea= BA.node[i]['EA']
        
        old_c = BA.node[i]['c']
        
        if old_c==0:
            BA.node[i]['c'] = 0
        elif rho==old_rho:
            continue
            #print ea * (1 - math.exp(-alpha * rho)) 
        elif ((old_c!=0) & (rho > old_rho)):
            BA.node[i]['c'] -= (old_ea - ea) 
 

def get_node_rho2(ba):
    return get_default_num(ba) / ba.number_of_nodes()
 
def update_nodes_c3(BA,g,alpha):
    for i in g.nodes():
        old_rho = BA.node[i]['rho']
        BA.node[i]['rho'] = get_node_rho2(BA)
        rho = BA.node[i]['rho']
        
        old_ea = BA.node[i]['EA']
        BA.node[i]['EA'] = BA.node[i]['EA'] * math.exp(-0.1 * rho)
        ea= BA.node[i]['EA']

        old_c=BA.node[i]['c']
        
        if old_c==0:
            BA.node[i]['c'] = 0
        elif rho==old_rho:
            continue
        elif ((old_c!=0) & (rho > old_rho)):
            BA.node[i]['c'] -= (old_ea - ea) 
            

def update_nodes_c2(BA,g,alpha):
    for i in g.nodes():
        old_rho = BA.node[i]['rho']
        BA.node[i]['rho'] = get_node_rho(g, i)
        rho = BA.node[i]['rho']

        old_ea = BA.node[i]['EA']
        BA.node[i]['EA'] = BA.node[i]['EA'] * math.exp(-alpha * rho)
        ea= BA.node[i]['EA']
        
        old_c = BA.node[i]['c']
        
        if old_c==0:
            BA.node[i]['c'] = 0
        elif rho==old_rho:
            continue
            #print ea * (1 - math.exp(-alpha * rho)) 
        elif ((old_c!=0) & (rho > old_rho)):
            BA.node[i]['c'] -= (old_ea - ea) 
            

def get_node_rho(g, node):
    neibor_num = len(g.node[node]['neibor'])
    #print 'has %d neibors' % (neibor_num)

    #nndn = neibor_num - g.node[node]['ndn']
    ndn = g.node[node]['ndn']
    #print 'default %d in neibors' % (g.node[node]['ndn'])
    
    #print 'the rho is %s' % (str(ndn / neibor_num))
    return ndn / neibor_num

def update_impact_between_nodes(G,ST):
    #print 'update s'
    for i in G.edges():
      #print i
      first = i[1]
      end = i[0]
      last_c = G.node[first]['c']
      last_S = G.node[first]['S']
      last_B = G.node[first]['B']
      #L = G.node[first]['L']
      L = G.node[first]['L']
      last_E = G.edge[end][first][0]['e']
      
      if last_c > last_S:
        ST.edge[first][end][0]['shock'] = 0
      elif last_S - last_c >= last_B:
        ST.edge[first][end][0]['shock'] = last_E
      else:
        ST.edge[first][end][0]['shock'] = (last_S - last_c) * last_E / 0.2
# update the impact from i node to j node in G
# by the change of status and 'c' value
def update_impact_between_nodes2(G,ST):
    for i in ST.edges():
      first = i[0]
      end = i[1]
      last_c = G.node[first]['c']
      last_S = G.node[first]['S']
      last_B = G.node[first]['B']
      if (end,first) in G.edges():
        last_E = G.edge[end][first][0]['e']
      else:
        last_E = 0
      L = G.node[first]['L']
      if last_c > last_S:
        ST.edge[first][end][0]['shock'] = 0
      elif last_S - last_c >= last_B:
        ST.edge[first][end][0]['shock'] = last_E
      else:
        ST.edge[first][end][0]['shock'] = (last_S - last_c) * last_E / L
  
# calculate the 'S' value of all nodes in G
# by the change of 's' value of edges in ST  
def update_nodes_S(G,ST):
    for i in G.nodes():
      G.node[i]['S'] = 0
      for j in ST.nodes():
        if j!=i:
          G.node[i]['S'] += ST.edge[j][i][0]['shock']

# set the 'S' value of node in G as 1
# from the list 'm', which contains a list of banks
def set_nodes_S(G,m):
    for i in m:
      G.node[i]['S'] = 1

# after loops, calculate the number of default banks.
def get_default_num(G):
    counter = 0
    for i in G.nodes():
      if G.node[i]['status'] == 'Default':
        counter += 1
    return counter

# package function, to build a directed BA graph,
# and initialize the 'c', 'S', 'L', 'B', 'status' value of all nodes in G
# and initialize the 'e' value of all edges in G 
def build_myBA(n,n0):
    myBA = build_network(n,n0)
    return myBA

def init_myBA(myBA, c_list, S_init_list):
    init_edges_attr_e(myBA)
    init_nodes_LB(myBA)
    init_nodes_rho(myBA)
    init_nodes_EA(myBA)
    init_nodes_CS(myBA,c_list,S_init_list) 
    init_nodes_status(myBA)
    return myBA

def init_nodes_EA(myBA):
    for i in myBA.nodes():
        myBA.node[i]['EA'] = 0.8

def init_nodes_rho(myBA):
    for i in myBA.nodes():
        myBA.node[i]['rho'] = 0

# package function, to build a complete directed graph 
# and initialize the 'shock' value of all edges in ST
def build_ST(n):
    ST = nx.complete_graph(n, create_using = nx.MultiDiGraph())
    return ST
    
def init_ST(ST):
    init_impact_between_nodes(ST)
    return ST


def get_max_degree_nodes(G, m):
    degree_list = []
    m_list = []
    n = G.number_of_nodes()
    for i in G.nodes():
      degree_list.append({'num':i,'degree':G.degree(i)})
    #print degree_list

    for i in range(0,n):
      for j in range(1, n):
        if degree_list[j-1]['degree'] < degree_list[j]['degree']:
          degree_list[j],degree_list[j-1] = degree_list[j-1],degree_list[j]

    for i in range(0,n):
      #print 'node %d, degree: %d' %(degree_list[i]['num'], degree_list[i]['degree'])
      m_list.append(degree_list[i]['num'])
    return m_list[0:m]

def get_min_degree_nodes(G, m):
    degree_list = []
    m_list = []
    n = G.number_of_nodes()
    for i in G.nodes():
      degree_list.append({'num':i,'degree':G.degree(i)})
    #print degree_list

    for i in range(0,n):
      for j in range(1, n):
        if degree_list[j-1]['degree'] > degree_list[j]['degree']:
          degree_list[j],degree_list[j-1] = degree_list[j-1],degree_list[j]

    for i in range(0,n):
      #print 'node %d, degree: %d' %(degree_list[i]['num'], degree_list[i]['degree'])
      m_list.append(degree_list[i]['num'])
    return m_list[0:m]

def get_max_indegree_nodes(G, m):
    degree_list = []
    m_list = []
    n = G.number_of_nodes()
    for i in G.nodes():
      degree_list.append({'num':i,'degree':G.in_degree(i)})
    #print degree_list

    for i in range(0,n):
      for j in range(1, n):
        if degree_list[j-1]['degree'] < degree_list[j]['degree']:
          degree_list[j],degree_list[j-1] = degree_list[j-1],degree_list[j]

    for i in range(0,n):
      m_list.append(degree_list[i]['num'])
    return m_list[0:m]


def get_max_outdegree_nodes(G, m):
    degree_list = []
    m_list = []
    n = G.number_of_nodes()
    for i in G.nodes():
      degree_list.append({'num':i,'degree':G.out_degree(i)})
    #print degree_list

    for i in range(0,n):
      for j in range(1, n):
        if degree_list[j-1]['degree'] < degree_list[j]['degree']:
          degree_list[j],degree_list[j-1] = degree_list[j-1],degree_list[j]

    for i in range(0,n):
      m_list.append(degree_list[i]['num'])
    return m_list[0:m]

def get_average_degree(G):
    num = G.number_of_nodes() 
    total = 0
    for i in G.nodes():
        total += G.degree(i)
    return total/num

def get_nodes_in_degree(G):
    result = []
    n = G.number_of_nodes()
    for i in range(0, n):
        result.append({'node':i, 'indegree':G.in_degree(i)})
    return result 

#convert a mutidigraph to a undirected graph (with no parallel edges)
def multidi_to_graph(G):
    '''
    edges = G.edges()
    for one in edges:
        rev = (one[1],one[0])
        if rev in edges:
            edges.remove(rev)
    edges = list(set(edges))
    G1 = nx.Graph()
    G1.add_edges_from(edges)
    '''
    G1 = nx.MultiGraph()
    G1.add_edges_from(G.edges())
    return G1

def get_neighbor_nodes(G, node):
    result = []
    for i in G.edges():
        if node == i[0]:
            result.append(i[1])
        elif node == i[1]:
            result.append(i[0])
    return list(set(result))

# G is an undirected graph, add its nodes until its average degree comes to d 
def add_graph_edges(G, m, d):
    if d >= G.number_of_nodes():
        print 'unreachable degree given!'
        sys.exit(1)

    for i in G.nodes():
        G.node[i]['dirty'] = 0
    n = G.number_of_nodes()
    repeated = []
    source = 0

    for i in G.edges():
        nodes = [i[0], i[1]]
        repeated.extend(nodes)

    while (get_average_degree(G) < d):
        if source == n:
            source = 0
        neibor = get_neighbor_nodes(G, source)
        #exclude = neibor.append(source)
        new = repeated[:]

        while(source in new):
            new.remove(source)

        ''' 
        for i in neibor:
            while(i in new):
                new.remove(i)
        '''

        flag = False
        if len(set(new)) <= m:
            #print 'this node is too big!'
            G.node[source]['dirty'] = 1
            for i in G.nodes():
                if G.node[i]['dirty'] == 0:
                    flag = True
            if flag == False:
                print 'FAIL to add nodes, too big degree'
                print 'largest degree is %d' % (get_average_degree(G))
                #print G.edges()
                sys.exit(4)
            source += 1
            continue
        #print new  
        targets = nx.random_graphs._random_subset(new, m)

        edges = zip([source]*m, targets)
       
        G.add_edges_from(edges)
        #print 'these edges are added: %s' % (edges)
        
        repeated.extend([source]*m)
        repeated.extend(targets)
        source += 1

def build_myG(myBA, n0, d):
    myG = multidi_to_graph(myBA)
    add_graph_edges(myG, n0, d)
    
    for i in myG.nodes():
        myG.node[i]['neibor'] = get_neighbor_nodes(myG, i)
    return myG

def init_myG(G):
    for i in G.nodes():
        G.node[i]['ndn'] = 0

if __name__ == '__main__':
    G = build_network(30,4)
    print 'number of edges of G is %d' % (G.number_of_edges())
    #print G.edges()
    print 'average degree is %d' % (get_average_degree(G))
    
    G1 = multidi_to_graph(G)
    print 'number of edges of G is %d' % (G1.number_of_edges())
    #print G1.edges()
    print 'average degree is %d' % (get_average_degree(G1))

    add_graph_edges(G1, 4, 13)
    print 'number of edges of G is %d' % (G1.number_of_edges())
    #print G1.edges()
    print 'average degree is %d' % (get_average_degree(G1))
        
    




