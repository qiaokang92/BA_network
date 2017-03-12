import networkx as nx
import random
from read_from_excel import *

chaijie_path = "./excel/chaijie_mat.xlsx"
gailu_path = "./excel/gailu_mat.xlsx"
hand_list = {(32,148),
                  (3,149),
                  (80,150),
                  (45,151),
                  (43,152),
                  (0,153),
                  (1,154),
                  (82,155),
                  (84,156),
                  (11,157),
                  (131,159),
                  (54,162),
                  (109,164),
                  (128,166),
                  (127,167),
                  (142,168)}


def get_graph_from_mat(G):    
    mat1 = get_mat(chaijie_path)
    mat2 = get_mat(gailu_path)
    names = get_all_names(chaijie_path)

    len1 = len(mat1)
    len2 = len(mat2)
    len3 = len1

    #G = nx.Graph()
    G.add_nodes_from(range(len1))

    edge_list1 = add_edges_from_mat1(G, mat1)
    edge_list2 = add_edges_from_mat2(G, mat2, edge_list1)
    add_edges_by_hand(G, hand_list)
    
    return edge_list1, edge_list2, hand_list

def add_edges_by_hand(G, hand_list):
    G.add_edges_from(hand_list)

def add_edges_by_hand_to_myG(G, hand_list):
    G.add_edges_from(hand_list)
    
def add_edges_from_mat1(G, mat1):
    len1 = len(mat1)
    node_list1 = []
    for i in range(0, len1):
        for j in range(i+1, len1):
            if(mat1[i][j] != 0):
                G.add_edge(i,j)
                node_list1.append((i,j))
    return node_list1

def add_edges_from_mat2(G, mat2, node_list1):
    len2 = len(mat2)
    node_list2 = []
    for i in range(0, len2):
        for j in range(i+1, len2):
            if((i,j) in node_list1):
                continue
            elif(build_an_edge(mat2[i][j])):
                G.add_edge(i,j)
                node_list2.append((i,j))
            else:
                continue
    return node_list2

def add_edges_to_myG(G, mat2, node_list1):
    len2 = len(mat2)
    node_list2 = []
    for i in range(0, len2):
        for j in range(i+1, len2):
            if((i,j) in node_list1):
                continue
            elif(build_an_edge(mat2[i][j])):
                G.add_edge(i,j)
                node_list2.append((i,j))
            else:
                continue
    return node_list2

def get_names():
    return get_all_names(gailu_path)

def build_an_edge(x):
    r = random.random()
    if (r < x):
        return True
    else:
        return False

def main():
    G = nx.Graph()
    list1,list2 = get_graph_from_mat(G)
    print G.nodes()
    print len(G.edges())
    print len(list1)
    print len(list2)
    
if __name__ == "__main__":
    main()
