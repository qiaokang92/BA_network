import matplotlib.pyplot as plt
from invoke import *
from gen_graph import *
from static_struct import *

g_path = './result/graphs.pkl'

def get_max_degree(G):
    return G.degree(get_max_degree_nodes(G,1)[0])

def get_color_list(G):
    n = G.number_of_nodes()
    max_degree = get_max_degree(G)
    colors = []

    for i in G.nodes():
        print G.degree(i)
        colors.append(G.degree(i) * n / max_degree)
    return colors

if __name__ == "__main__":
    myBA, ST, myG = get_graphs_from_file(g_path)
    G = multidi_to_graph(myBA)
    colors = get_color_list(G)
    
    nx.draw(G, node_color=colors, cmap=plt.cm.Reds, node_size=30)
    plt.show()

