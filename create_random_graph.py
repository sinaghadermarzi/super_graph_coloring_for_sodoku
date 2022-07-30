import random
import scipy
import csv
from matplotlib import pyplot
import os






def random_combination(iterable, r):
    "Random selection from itertools.combinations(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(xrange(n), r))
    return tuple(pool[i] for i in indices)


def create_graph(v,e):
    edges_gen = [];

    for i in range(1,2*e):
        r = random_combination(range(1, v+1), 2)
        edges_gen.append(r);


    for s in edges_gen:
            while edges_gen.count(s)>1:
                edges_gen.pop(edges_gen.index(s))
            rs = reversed(s)
            while edges_gen.count(rs)>0:
                edges_gen.pop(edges_gen.index(rs))

    edges = edges_gen[0:e]
    deg = []
    for k in range(0,v):
        deg.append(0)

    for ed in edges:
        deg[ed[0]-1]+=1
        deg[ed[1]-1]+=1
    maxdeg= max(deg)

    filename="graph_"+str(v)+"_"+str(e)+"_"+str(maxdeg)+".txt"
    f = open(filename,"w")

    f.write(str(v)+' '+str(e)+'\n')
    for edge in edges:
        f.write(str(edge[0])+' '+str(edge[1])+'\n')


    colors = ''
    for i in range(0,v):
        colors = colors+"0 "
    colors = colors.rstrip(' ')
    f.write(colors + '\n')
    f.close()



create_graph(50,500)
create_graph(100,1000)
create_graph(200,2000)
create_graph(500,5000)