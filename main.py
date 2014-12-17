import networkx as nx
import sys
import os 
import signal
import time
from static_struct import *
from purpose_attack import *
from random_attack import *
from test import *

def do_attack(opts, args):
    if opts.mode == 't':
        print 'Mode: test'
        self_test(opts)
    elif opts.mode == 'r':
        print 'Mode: random attack'
        do_random_attack(opts)
    elif opts.mode == 'p':
        print 'Mode: purpose attack'
        do_purpose_attack(opts)
    else:
       print 'error: wrong mode type!'
       sys.exit(1)

if __name__ == '__main__':
    opts, args = parse_options()
    do_attack(opts, args)
