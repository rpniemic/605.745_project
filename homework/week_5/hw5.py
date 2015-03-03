#!/usr/bin/env python

# over arching algorithm
# http://bayes.cs.ucla.edu/BOOK-2K/d-sep.html

import sys

def main (filename):
    graph,start,finish,conditions = parse(filename)

    answer = bayes_balls(graph, [start], conditions)
    
    return answer

def bayes_balls (G, F, K):
    visited = [False for i in G]
    mk_top = [False for i in G]
    mk_bottom = [False for i in G]
    
    schedule = []
    
    while len(schedule) > 0:
        j = schedule.pop()
        visited[j] = True
        
        if j not in K:
    
    
    
#new_graph = apply_conditions(graph, conditions)

#return not path_exists(new_graph, start, finish)

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
    ug = make_undirected(graph)
    return ug
    
    
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
