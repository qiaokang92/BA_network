from __future__ import division
import xlrd
import numpy as np
import scipy as sp

def open_excel(excel_file):
    try:
        data = xlrd.open_workbook(excel_file)
        return data
    except Exception,e:
        print str(e)

def get_BA_data_from_excel(init_path, n):
    data = open_excel(init_path)
    table = data.sheets()[0]

    l_list = [0] * n
    b_list = [0] * n
    c_list = [0] * n
    ea_list = [0] * n
    TA_list = [0] * n
    rows = n

    for i in range(1, rows + 1):
        row = table.row_values(i)
        l_list[i-1] = row[2]
        b_list[i-1] = row[3]
        c_list[i-1] = row[4]
        ea_list[i-1] = row[5]
        TA_list[i-1] = row[6]

    return l_list, b_list, c_list, ea_list, TA_list

def get_kind_ids(i, init_path):
    data = open_excel(init_path)
    table = data.sheets()[0]
    kind_list = []

    if i==1:
        for i in range(2,6):
            row = table.row_values(i)
            kind_list.append(int(row[8]) - 1)
        return kind_list

    if i==2:
        for i in range(2,17):
            row = table.row_values(i)
            kind_list.append(int(row[9]) - 1)
        return kind_list

    if i==3:
        for i in range(2,43):
            row = table.row_values(i)
            kind_list.append(int(row[10]) - 1)
        return kind_list

    if i==4:
        for i in range(2,72):
            row = table.row_values(i)
            kind_list.append(int(row[11])- 1)
        return kind_list

    if i==5:
        for i in range(2,18):
            row = table.row_values(i)
            kind_list.append(int(row[12]) - 1)
        return kind_list

    if i==6:
        kind_list = range(149,170)
        return kind_list

def get_all_names(excel_file):
    data = open_excel(excel_file)
    table = data.sheets()[1]

    nrow = table.nrows
    names = []

    for i in range(0, nrow):
        row = table.row_values(i)
        name = row[1]
        names.append(str(name))

    return names

def get_mat(f):
    data = open_excel(f)
    table = data.sheets()[0]
    
    nrows = table.nrows
    ncols = table.ncols

    #print "parsing file: %s" % f
    #print " there are %d rows" % nrows
    #print " there are %d cols" % ncols
    chaijie_mat = np.identity(nrows)
    
    a = table.row_values(0)

    for i in range(0, nrows):
        row = table.row_values(i)
        for j in range(0, ncols):
            chaijie_mat[i][j] = float(row[j])
    return chaijie_mat

def get_all_data(excel_file):
    data = open_excel(excel_file)
    table = data.sheets()[0]
    
    nrows = table.nrows
    ncols = table.ncols

    head = table.row_values(0)
    all_data = []

    for i in range(1, nrows - 1):
        row = table.row_values(i)
        all_data.append(dict(ID = int(row[1]), B = row[2], L = row[3]))

    return all_data

def main():
    #print get_all_data("./excel/data2014.xls")
    #print get_all_names("./excel/chaijie_mat.xlsx")
    print get_mat("./excel/chaijie_mat.xlsx")
    print get_mat("./excel/gailu_mat.xlsx")
    
if __name__ == "__main__":
    main()

