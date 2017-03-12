from get_graph_from_mat import *
import networkx as nx
import numpy as np
import xlwt

def write_to_excel(mat, n, fname):
    file1 = xlwt.Workbook()
    table1 = file1.add_sheet('sheet1')

    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                table1.write(i,j,1)
            else:
                table1.write(i,j,0)

    file1.save('./excel/mat-0-1.xls')

if __name__ == "__main__":
    G = nx.Graph()
    list1,list2,list3 = get_graph_from_mat(G)

    n = 170
    mat = np.identity(n)
    for i in range(n):
        for j in range(n):
            mat[i][j] = 0
    
    for i in list2:
        x = i[0]
        y = i[1]
        mat[x][y] = 1
        mat[y][x] = 1

    for i in list3:
        x = i[0]
        y = i[1]
        mat[x][y] = 1
        mat[y][x] = 1

    write_to_excel(mat, n, 'level2-0-1')


