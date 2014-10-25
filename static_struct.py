import networkx as nx

def build_network(n,m):
    return nx.random_graphs.my_BA_graph(n,m)

def get_edges_attr(G):
    result = []
    for i in G.edges():
      start = i[0]
      to = i[1]
      show = G[start][to][0]
      show['edge'] = i
      result.append(show)
    return result
      
def get_edge_attr(G,edge):
    start = edge[0]
    end = edge[1]
    attr = G[start][end][0]
    return attr
      
def get_nodes_attr(G):
    result = []
    for i in G.nodes():
      show = G.node[i]
      show['node'] = i
      result.append(show)
    return result

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
    
def init_nodes_LB(G):
    for i in G.nodes():
      result = 0
      for j in G.edges():
        if i == j[0]:
          result += get_edge_attr(G,j)['e']
      G.node[i]['L'] = 0.2
      G.node[i]['B'] = result

#receive 2 lists with n elements, like [0.6, 0.7, ...]
def init_nodes_CS(G,c,s):
    for i in G.nodes():
      G.node[i]['c'] = c[i]
      G.node[i]['S'] = s[i]

def init_nodes_S(G,m_list):
    for i in m_list:
      G.node[i]['S'] = 1

def init_nodes_status(G):
    for i in G.nodes():
      G.node[i]['status'] = 'Stable'

def init_impact_between_nodes(ST):
    for i in ST.edges():
      start = i[0]
      to = i[1]
      ST[start][to][0]['shock'] = 0

def update_nodes_status(G):
    for i in G.nodes():
      if G.node[i]['c'] > G.node[i]['S']:
        G.node[i]['c'] -= G.node[i]['S']
        G.node[i]['status'] = 'Stable'
      else:
        G.node[i]['c'] = 0
        G.node[i]['status'] = 'Default'

def update_impact_between_nodes(G,ST):
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
    
def udpate_nodes_S(G,ST):
    n = len(G)
    for i in G.nodes():
      G.node[i]['S'] = 0
      for j in ST.nodes():
        if i != j:
          G.node[i]['S'] += ST.edge[j][i][0]['shock']

def set_nodes_S(G,m):
    for i in m:
      G.node[i]['S'] = 1

def get_default_num(G):
    counter = 0
    for i in G.nodes():
      if G.node[i]['status'] == 'Default':
        counter += 1
    return counter








