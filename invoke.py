from optparse import OptionParser
import pickle
import signal
import sys
import time
import os
from static_struct import *
import  matplotlib.pyplot as plt
#from attack_invoke import *

def signal_handler(signal, frame):
    print '\nProgram Exit'
    sys.exit(0)

def parse_options():
    signal.signal(signal.SIGINT, signal_handler)
   
    parser = OptionParser(usage = '\n    python %prog -n number_of_banks [options]', 
                          description = 'this algorithm aimed ......')
    
    parser.add_option("-n", "--num-banks", dest = "bank_number",
                            type = "int",
                            help = "The number of banks")

    parser.add_option("-i", dest = "step",
                            action = 'store',
                            type = 'int',
               help = "nodes connected every step, default is 1")
   
    parser.add_option("-m", dest = 'attack_number',
                            action = 'store',
                            type = 'int',
          help = 'Once this option is given, m banks will be give a shock as 1')

    parser.add_option("-g","--num-graph", dest = 'num_graph',
                                action = 'store',
                                type = 'int',
                                default = 1,
                                help = "how many BA networks do you want to test")
    
    parser.add_option("-t","--random-times",dest = 'random_times',
                                 action = 'store',
                                 type = 'int',
                                 default = '1',
                        help = 'in random mode, repeat times for a single network')

    parser.add_option( "-f","--figure-kind", dest = 'figure_kind',
                                 action = 'store',
                                 type = 'string',
                                 default = 'line',
                        help = 'figure types you want, can be line or points')
    
    parser.add_option( "--lamuta", dest = "lamuta",
                                type = "float",
                                action = 'store',
                                default = 0.06,
                         help = 'Banks\' initial property')

    parser.add_option("--loop", dest = "max_loop",
                               action = 'store',
                               type = 'int',
                         help = 'maximum times the loop does')

    parser.add_option("-M","--attack-mode", dest = "mode",
                                action = 'store',
                                type = 'string',
                                help = 'test, purpose or random')

    parser.add_option("-d", "--degree", dest = "degree",
                               action = "store",
                               type = "string",
                               help = "in, out, or all")

    parser.add_option("-a", "--action", dest="action",
                               action = "store",
                               default = "no",
                               help = "no, info, no+info")

    parser.add_option("--data", dest="data_path",
                               action="store",
                               type="string",
                               default="./result/data.pkl")

    parser.add_option("--txt", dest="txt_path",
                                action = 'store',
                                type = 'string',
                                default = '')

    (options, args) = parser.parse_args()
   
    #print options.bank_number
    #print type(options.bank_number)

    if not options.bank_number:
      parser.error('total number of banks is not given')
    
    if not options.attack_number:
      parser.error('how many banks do you want to attack?')

    if not options.mode:
      parser.error('attack mode unknown!')
    
    print 'Total number is: %d' % (options.bank_number)
    print 'Every step is: %d' % (options.step)
    print 'Banks will be attacked: %d' % (options.attack_number)
    print 'Attack mode: %s' % (options.mode)

    return options, args

def gen_figure(data, figure_kind):
    for i in data:
      if len(i) != 0:
        draw_figure(i, figure_kind, 'o-')
    plt.show()

def draw_figure(result, kind, line):
    groups = len(result)
    times = len(result[0])
    lens = len(result[0][0])
    
    if kind == 'single_line':
      ave1 = get_average_list_1(result)
      ave = get_average_list_2(ave1)
      index = range(1, lens+1)
      plt.plot(index, ave, line)
      #plt.show()
    
    elif kind == 'lines':
      index = range(1, lens+1)
      for i in range(0, groups):
        for j in range(0, times):
          plt.plot(index, result[i][j], line)
      #plt.show()

    elif kind == 'points':
      index = range(1, lens+1)
      for i in range(0, groups):
        for j in range(0, times):
          plt.plot(index, result[i][j], 'o', line)

def get_average_list_1(result):
    groups = len(result)
    times = len(result[0])
    lens = len(result[0][0])
    result2 = []

    for k in range(0, groups):
        result1 = []
        for i in range(0, lens):
            total = 0
            for j in range(0,times):
                total += result[k][j][i]
            result1.append(total / times)
        result2.append(result1)
    
    return result2

def get_average_list_2(result):
    groups = len(result)
    lens = len(result[0])
    num = []

    for i in range(0,lens):
        total = 0
        for j in range(0, groups):
            total += result[j][i]
        num.append(total / groups)
    return num

def sava_data(all_data, path):
    output = open(path, 'wb')
    pickle.dump(output, all_data)
    output.close()

def get_simple_result(result):
    ave1 = get_average_list_1(result)
    ave = get_average_list_2(ave1)
    return ave

def write_data_2_txt(fname, all_data):
    data1 = all_data[0][0]
    data2 = all_data[0][1]

    times1 = all_data[1][0]
    times2 = all_data[1][1]

    result_txt1 = './result/' + fname + '_result_no_info.txt'
    result_txt2 = './result/' + fname + '_result_with_info.txt'
    time_txt1 = './result/' + fname + '_time_no_info.txt'
    time_txt2 = './result/' + fname + '_time_with_info.txt'
    
    ave_result1 = get_simple_result(data1)
    ave_result2 = get_simple_result(data2)
    ave_times1 = get_simple_result(times1)
    ave_times2 = get_simple_result(times2)
    
    write_one_data_2_txt(result_txt1, ave_result1)
    write_one_data_2_txt(result_txt2, ave_result2)
    write_one_data_2_txt(time_txt1, ave_times1)
    write_one_data_2_txt(time_txt2, ave_times2)

def write_one_data_2_txt(path, data):
    f = open(path , 'w') 
    for i in data:
        f.write(str(i))
        f.write(' ')
    f.close()

def save_data(path, all_data):
    data1 = all_data[0][0]
    data2 = all_data[0][1]

    #times1 = all_data[1][0]
    #times2 = all_data[1][1]

    output = open(path, 'a')

    ave_result1 = get_simple_result(data1)
    ave_result2 = get_simple_result(data2)
    
    pickle.dump(ave_result1, output)
    pickle.dump(ave_result2, output)

