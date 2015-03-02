#!/usr/bin/env python

# over arching algorithm
# http://bayes.cs.ucla.edu/BOOK-2K/d-sep.html

import sys

def main (filename):
    graph,start,finish,conditions = parse(filename)
        
    new_graph = apply_conditions(graph, conditions)
        
    return not path_exists(new_graph, start, finish)

def parse (filename):
    with open(filename, 'rb') as f:
        raw = f.read().strip().split(':')
    
    str_graph = raw[0].split(',')
    str_nodes = raw[1].split(',')
    str_conditions = raw[2].split(',')
    
    graph = [[int(s) for s in row] for row in str_graph]
    start = int(str_nodes[0])-1
    finish = int(str_nodes[1])-1
    conditions = [int(sc)-1 for sc in str_conditions]

    return graph, start, finish, conditions
        
def apply_conditions (graph, conditions):
    colliders = find_colliders(graph)
    is_ok = [c in conditions for c in colliders]
    
    print 'conditions', conditions
    print 'colliders', colliders
    print 'is_ok', is_ok

    #trimmed_graph = remove_collitions(graph, colliders, is_ok)
    
    return None

def find_colliders (graph):
    colliders = []
    for i in xrange(len(graph)):
        incoming = sum([row[i] for row in graph])
        if incoming >= 2: colliders.append(i)
    return colliders
    
def make_undirected (d_graph):
    u_graph = [[value for value in row] for row in d_graph]
    
    for i,row in enumerate(d_graph):
        for j, value in enumerate(row):
            if value == 1: u_graph[j][i] = 1

    return u_graph

def path_exists (graph, start, finish):
    # short circuited BFS to check for path existance
    # https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode

    queue = [start]
    explored = [start]
    while True:
        if len(queue) == 0: return False
        v = queue.pop(0)
        
        for w, val in enumerate(graph[v]):
            if val == 0: continue
            if w == finish: return True # short circuit
            if w not in explored:
                queue.append(w)
                explored.append(w)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 1:
        print 'Error: No input file given'
    else:
        print 'Error: too many inputs given'
