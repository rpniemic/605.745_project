#!/usr/bin/env python

import sys

def main (filename):
    graph,start,finish,conditions = parse(filename)
    
    new_graph = apply_conditions(graph, conditions)
    
    route = find_route(new_graph, start, finish)
    
    if route is None:
        print 'False'
    else:
        print 'True'

def apply_conditions (graph, conditions):
    return None

def find_route (new_graph, start, finish):
    return None

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
        
if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 1:
        print 'Error: No input file given'
    else:
        print 'Error: too many inputs given'
