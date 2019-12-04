

import sys
import os
import resource

resource.setrlimit(resource.RLIMIT_STACK,(1024000,1024000))
sys.setrecursionlimit(2**20)

G = {}
t = 0
s = None

stack = []
explored = []
runtime = {}
scc = {}
top5 = []

def rev(G):
    G_rev = {}
    for tail in G.keys():
        for head in G[tail]:
            if head not in G_rev:
                G_rev[head] = []
            G_rev[head].append(tail)
    return G_rev

def arange_rev(G_rev):
    for i in range(1,875714+1):
        if i not in G_rev.keys():
            G_rev[i] = None
    return G_rev

def DFS_1st(G,i):
    print(i)
    global t
    explored.append(i)
    if not G[i]:
        t +=1
        runtime[i] = t
        return
    else:
        for j in G[i]:
            if j not in explored:
                DFS_1st(G,i)
        t += 1
        runtime[i] = t

    t += 1
    runtime[i]=t
    print(i)

def DFS_1st_loop(G):
    global t
    global s
    for i in range(875714,0,-1):
        if i not in explored:
            s = i
            DFS_1st(G,i)

def reorg_G(G,runtime):
    G_final = {}
    for i in G.keys():
        G_final[runtime[i]] = list(map(lambda x:runtime[x],G[i]))
    return G_final

with open('SCC.txt') as f:
    for line in f:
        line = line.split(' ')
        tail = int(line[0])
        head = int(line[1])
        if tail not in G.keys():
            G[tail]=[]
        G[tail].append(head)

G_temp = rev(G)
G_rev = arange_rev(G_temp)
with open('revGraph.txt','w') as f:
    for i in range(1,875714+1):
        if not G_rev[i]:
            f.writelines(str(i)+' '+' '+'\n')
        else:

            for head in G_rev[i]:
                f.writelines(str(i)+' '+str(head)+'\n')
exit()
DFS_1st_loop(G_rev)
print(runtime)
exit()


