#!/usr/bin/env python

# over arching algorithm
# http://bayes.cs.ucla.edu/BOOK-2K/d-sep.html

import sys

def main (filename):
    graph,start,finish,conditions = parse(filename)
    
    paths = find_all_paths(make_undirected(graph), start, finish)
    
    apply_conditions(graph, conditions, paths)
    
    if len(paths) > 0 : return False
    else: return True
    

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
    
def make_undirected (d_graph):
    u_graph = [[value for value in row] for row in d_graph]
    for i,row in enumerate(d_graph):
        for j, value in enumerate(row):
            if value == 1: u_graph[j][i] = 1
    return u_graph

def find_all_paths (graph, start, finish):

    paths = []
    q = [[start]]

    while len(q) > 0:
    	tmp_path = q.pop(0)
    	last_node = tmp_path[-1]
    	if last_node == finish:
            paths.append(tmp_path)
        for link_node, val in enumerate(graph[last_node]):
            if val == 0: continue
            if link_node not in tmp_path:
                new_path = tmp_path + [link_node]
                q.append(new_path)
    return paths

def apply_conditions (graph, conditions, paths):

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 1:
        print 'Error: No input file given'
    else:
        print 'Error: too many inputs given'
