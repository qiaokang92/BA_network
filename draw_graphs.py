import sys
import matplotlib.pyplot as plt
from invoke import *
from gen_graph import *
from static_struct import *
import networkx as nx
from get_graph_from_mat import *
import math

g_path = sys.argv[1]

def get_max_degree(G):
    return G.degree(get_max_degree_nodes(G,1)[0])

def get_node_size(G , node_list):
    n = G.number_of_nodes()
    max_degree = get_max_degree(G)
    colors = []

    for i in node_list:
        a = (math.sqrt( (G.degree(i)+1) * n / max_degree * 11))
        colors.append(a*10)
    return colors

def get_color_list(G , node_list):
    n = G.number_of_nodes()
    max_degree = get_max_degree(G)
    colors = []

    for i in node_list:
        colors.append(G.degree(i) * n / max_degree)
    return colors
def get_node_list(G):
    new_list = []
    for i in G.nodes():
        if G.degree(i) != 0:
            new_list.append(i)
    return new_list

def get_new_names(node_list, names):
    print len(node_list)
    print len(names)
    new = {}
    for i in node_list:
        new[i] = names[i]
    return new

if __name__ == "__main__":
    G = nx.Graph()
    list1, list2, list3 = get_graph_from_mat(G)
    print list3 
    #G = G.subgraph(range(0,50))
    
    #node_list = get_node_list(G)
    node_list = G.nodes()
    node_colors = get_color_list(G, node_list)
    edge_colors=[]
    
    for i in G.edges():
        if i in list1:
            edge_colors.append('g')
        elif i in list2:
            edge_colors.append('y')
        elif i in list3:
            edge_colors.append('y')
        else:
            print i
            print 'ERROR!'
            sys.exit(0)
    node_size = get_node_size(G, node_list) 
    names = get_names()
    new_names = get_new_names(node_list, names)
    pos = nx.spring_layout(G, k=0.25, scale=100)
    
    print len(node_list)
    plt.figure(figsize=(20,20))
    nx.draw_networkx_nodes(G, pos, node_color = node_colors, nodelist= node_list, node_size = node_size) 
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width = 1)
    nx.draw_networkx_labels(G, pos, labels = new_names, font_size = 7) 
     
    #plt.show()
    plt.savefig(g_path)

    '''
    myBA, ST, myG = get_graphs_from_file(g_path)
    BA = multidi_to_graph(myBA)
    G = multidi_to_graph(myG)
    node_colors = get_color_list(G)
    edge_colors=[]
    #print G.nodes()
    
    for i in G.edges():
        if i in BA.edges():
            edge_colors.append('k')
        else:
            edge_colors.append('y')
    
    #nx.draw(BA, node_color=colors, cmap=plt.cm.Reds, node_size=60)
    #nx.draw_networkx_nodes(G, node_color=colors, cmap=plt.cm.Blues, node_size=60)
    nx.draw(G, node_color=node_colors, cmap=plt.cm.Reds, edge_color=edge_colors, node_size=60)
    plt.show()
    '''
