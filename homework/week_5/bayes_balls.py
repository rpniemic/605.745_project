#!/usr/bin/env python

# over arching algorithm
# http://bayes.cs.ucla.edu/BOOK-2K/d-sep.html

import sys

def main (filename):
    graph,start,finish,conditions = parse(filename)

    Ni,_,_ = bayes_balls(graph, [], start, conditions)
    
    print finish
    
    print Ni

    print all([node in Ni for node in finish])
    

def parse (filename):
    with open(filename, 'rb') as f:
        raw = f.read().strip().split(':')
    
    str_graph = raw[0].split(',')
    str_start = raw[1].split(',')
    str_finish = raw[2].split(',')
    str_conditions = raw[3].split(',')
    
    graph = [[int(s) for s in row] for row in str_graph]
    start = [int(sn)-1 for sn in str_start if sn != '']
    finish = [int(fn)-1 for fn in str_finish if fn != '']
    conditions = [int(sc)-1 for sc in str_conditions if sc != '']

    if len(start) < 1:
        print 'Error: No start nodes given'
        exit()
    if len(finish) < 1:
        print 'Error: No finish nodes given'
        exit()

    return graph, start, finish, conditions
    
# see Shachter 1998 for details
def bayes_balls (G, F, J, K):
    
    visited = [False for node in G]
    marked_top = [False for node in G]
    marked_bottom = [False for node in G]
    direction = [set(['c']) if node in J else set() for node in xrange(len(G))]

    schedule = [node for node in J]
    
    while len(schedule) > 0:
        j = schedule.pop()
        
        visited[j] = True
        
        # c)
        if j not in K and 'c' in direction[j]:
            # i.
            if not marked_top[j]:
                marked_top[j] = True
                add_parents(get_parents(j,G), schedule, direction)
            # ii.
            if j not in F and not marked_bottom[j]:
                marked_bottom[j] = True
                add_children(get_children(j,G), schedule, direction)
        
        # d)
        if 'p' in direction[j]:
            # i.
            if j in K and not marked_top[j]:
                marked_top[j] = True
                add_parents(get_parents(j,G), schedule, direction)
            # ii.
            if j not in K and not marked_bottom[j]:
                marked_bottom[j] = True
                add_children(get_children(j,G), schedule, direction)
    
    Ni = [node for node, v in enumerate(marked_bottom) if not v]
    Np = [node for node, v in enumerate(marked_top) if v]
    Ne = [node for node in K if visited[node]]
    
    return Ni, Np, Ne                

def add_parents (parents, schedule, direction):
    for p in parents:
        if p not in schedule:
            schedule.append(p)
            direction[p].add('c')

def add_children (children, schedule, direction):
    for c in children:
        if c not in schedule:
            schedule.append(c)
            direction[c].add('p')

def get_parents (node, graph):
    return [parent for parent, row in enumerate(graph) if row[parent] == 1]

def get_children (node, graph):
    return [child for child, value in enumerate(graph[node]) if value == 1]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 1:
        print 'Error: No input file given'
    else:
        print 'Error: too many inputs given'
