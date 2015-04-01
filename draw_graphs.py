import matplotlib.pyplot as plt
from invoke import *
from gen_graph import *
from static_struct import *
import networkx as nx

g_path = './result/graph50.pkl'

def get_max_degree(G):
    return G.degree(get_max_degree_nodes(G,1)[0])

def get_color_list(G):
    n = G.number_of_nodes()
    max_degree = get_max_degree(G)
    colors = []

    for i in G.nodes():
        colors.append(G.degree(i) * n / max_degree)
    return colors

if __name__ == "__main__":
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

