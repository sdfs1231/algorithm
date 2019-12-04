import sys
import os
import resource

resource.setrlimit(resource.RLIMIT_STACK,(1024000,1024000))
sys.setrecursionlimit(2**20)
G_rev = {}
t = 0
runtime = {}
explored = []
with open('revGraph.txt','r') as f:
    for line in f:
        line = line.split(' ')
        tail = int(line[0])
        if line[1] == '':
            head = None
        else:
            head = int(line[1])
        if tail not in G_rev.keys():
            G_rev[tail] = []
        G_rev[tail].append(head)

def DFS_1st(G,i):
    global t
    global explored
    explored.append(i)
    if not G[i][0]:
        t += 1
        runtime[i] = t
        return None
    else:
        for j in G[i]:
            if j not in explored:
                DFS_1st(G,j)
        t += 1
        runtime[i] = t

def DFS_1st_loop(G):
    global t
    global explored
    for i in range(875714,0,-1):
        print('source node: %d'%i)
        if i not in explored:
            DFS_1st(G,i)


DFS_1st_loop(G_rev)
print(runtime)