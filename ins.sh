#!/bin/bash

N=150
M=25
T=5

rm result/data.pkl
rm result/graphs.pkl

python gen_graph.py -n $N -i 4 -m $M -t $T -M random -f single_line -a no+info

python main.py -n $N -i 4 -m $M -t $T -M random -f single_line -a no+info --txt=6 
python main.py -n $N -i 4 -m $M -t $T -M random -f single_line -a no+info --txt=4 --lamuta=0.04
python main.py -n $N -i 4 -m $M -t $T -M random -f single_line -a no+info --txt=8 --lamuta=0.08

python draw_figures.py
