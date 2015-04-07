#!/bin/bash
#same=0+0, use different m_list, same=0+1, use the same m_ist
#add=0, use random m_list, add=1, use add m_list
#kind=1, no info level, kind=2, with info level

N=500
M=50
T=50
alpha=0.06
t=4

GRAPH_PATH=./result/graph${N}-$t.pkl
DATA_PATH=./result/data${N}-$t.pkl
LIST_PATH=./result/list${N}-$t.pkl

rm ${DATA_PATH}
rm ${GRAPH_PATH}
rm ${LIST_PATH}

python gen_graph.py -n $N -i 1 --graph=${GRAPH_PATH} 

#python gen_m_list.py $LIST_PATH 20 2

python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.03 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=1 --list=${LIST_PATH} --same=0 --add=1
python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.03 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=2 --list=${LIST_PATH} --same=0 --add=1

python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.04 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=1 --list=${LIST_PATH} --same=0 --add=1
python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.04 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=2 --list=${LIST_PATH} --same=0 --add=1

python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.05 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=1 --list=${LIST_PATH} --same=0 --add=1
python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.05 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=2 --list=${LIST_PATH} --same=0 --add=1

python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.06 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=1 --list=${LIST_PATH} --same=0 --add=1
python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.06 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=2 --list=${LIST_PATH} --same=0 --add=1

python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.07 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=1 --list=${LIST_PATH} --same=0 --add=1
python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.07 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=2 --list=${LIST_PATH} --same=0 --add=1

python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.08 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=1 --list=${LIST_PATH} --same=0 --add=1
python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.08 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=2 --list=${LIST_PATH} --same=0 --add=1

python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.09 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=1 --list=${LIST_PATH} --same=0 --add=1
python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.09 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=2 --list=${LIST_PATH} --same=0 --add=1

python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.1 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=1 --list=${LIST_PATH} --same=0 --add=1
python main.py -n $N -i 2 -m $M -t $T -M random -f single_line -a no+info --txt=6-1 --lamuta=0.1 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=${alpha} --kind=2 --list=${LIST_PATH} --same=0 --add=1



python draw_figures.py ${DATA_PATH} 16

#python main.py -n $N -i 4 -m $M -t $T -M random -f single_line -a no+info --txt=4-15 --lamuta=0.04 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=0.15

#python main.py -n $N -i 4 -m $M -t $T -M random -f single_line -a no+info --txt=5-20 --lamuta=0.05 --graph=${GRAPH_PATH} --data=${DATA_PATH} --alpha=0.2

