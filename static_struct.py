'''
This file includes some functions for 2 graphs.
The first graph G is a graph of banks, the second one includes the strike between banks.
 
Author: Kang Qiao, BUAA
Finsh Date: Oct, 25th, 2014
'''
import random
import networkx as nx

'''
build a BA network, with n nodes and each step connet m nodes
this network is directed and have multiple edges
modified from barabasi_albert_graph() in networkx.random_graphs module
'''

def build_network(n,m):
    return nx.random_graphs.my_BA_graph(n,m)

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

def get_nodes_attr_c(G):
    result = []
    for i in G.nodes():
      show = G.node[i]
      result.append(show['c'])
    return result

# init the 'e' value of all edges in G 
def init_edges_attr_e(G):
    for i in G.edges():
      first = i[0]
      to = i[1]
      to_in = G.in_degree(to)
      if (to_in): 
        G.edge[first][to][0]['e'] = 0.2 /to_in 
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
      G.node[i]['L'] = result2
      G.node[i]['B'] = result

#  init the 'c' and 'S' value of all nodes in G
#  receive 2 lists, each has n elements, like [0.6, 0.7, ...]
def init_nodes_CS(G,c,s):
    for i in G.nodes():
      G.node[i]['c'] = c[i]
      G.node[i]['S'] = s[i]

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
def update_nodes_status(G):
    for i in G.nodes():
      if G.node[i]['c'] > G.node[i]['S']:
        G.node[i]['c'] -= G.node[i]['S']
        G.node[i]['status'] = 'Stable'
      else:
        G.node[i]['c'] = 0
        G.node[i]['status'] = 'Default'

def update_impact_between_nodes(G,ST):
    for i in G.edges():
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
        ST.edge[first][end][0]['shock'] = (last_S - last_c) * last_E / L

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
def udpate_nodes_S(G,ST):
    n = len(G)
    for i in G.nodes():
      G.node[i]['S'] = 0
      for j in ST.nodes():
        if i != j:
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
    init_nodes_CS(myBA,c_list,S_init_list) 
    init_nodes_status(myBA)
    return myBA

# package function, to build a complete directed graph 
# and initialize the 'shock' value of all edges in ST
def build_ST(n):
    ST = nx.complete_graph(n, create_using = nx.MultiDiGraph())
    return ST
    
def init_ST(ST):
    init_impact_between_nodes(ST)
    return ST

def get_random_list(n,m):
    n_list = range(0,n)
    m_list =  random.sample(n_list,m)
    return m_list

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
      m_list.append(degree_list[i]['num'])
    return m_list[0:m]

def get_average_degree(G):
    num = G.number_of_nodes() 
    total = 0
    for i in G.nodes():
        total += G.degree(i)
    return total/num








