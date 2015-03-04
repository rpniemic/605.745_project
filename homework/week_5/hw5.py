#!/usr/bin/env python

# over arching algorithm
# http://bayes.cs.ucla.edu/BOOK-2K/d-sep.html

import sys

def main (filename):
    graph,start,finish,conditions = parse(filename)

    print
    print 'Graph'
    for row in graph: print '  ', row
    print
    print 'Start: {}, Finish: {}'.format(start, finish)
    print
    print 'Conditions: [{}]'.format(', '.join([str(node) for node in conditions]))
    print

    possible_paths = find_all_paths(make_undirected(graph), start, finish)
    
    print 'Possible Paths'
    for p in possible_paths: print '  ', p
    print 

    valid_paths = [p for p in possible_paths if valid_path(graph, conditions, p)]

    print 'Valid Paths'
    for p in valid_paths: print '  ', p
    print 
    
    if len(valid_paths) > 0:
        print 'False'
        return False
    else:
        print 'True'
        return True
    

def parse (filename):
    with open(filename, 'rb') as f:
        raw = f.read().strip().split(':')
    
    str_graph = raw[0].split(',')
    str_nodes = raw[1].split(',')
    str_conditions = raw[2].split(',')
    
    graph = [[int(s) for s in row] for row in str_graph]
    start, finish = int(str_nodes[0])-1, int(str_nodes[1])-1
    conditions = [int(sc)-1 for sc in str_conditions if sc != '']

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

def valid_path (g, c, p):

    print '\tPath Checking'
    print '\t  ', p

    if len(p) <= 2:
        return corner_case(g,c,p)
    else:
        for s,m,t in sliding_window(p, 3):
            dir_1, dir_2 = g[s][m], g[m][t]

            if violates_rule1(dir_1, dir_2, m in c):
                arrow = '->' if dir_1 == 1 else '<-'
                print '\t  Violates rule 1 at {}{}{}{}{} given {}\n'.format(s,arrow,m,arrow,t,m)
                return False
            elif violates_rule2(dir_1, dir_2, m in c):
                print '\t  Violates rule 2 at {}<-{}->{} given {}\n'.format(s,m,t,m)
                return False
            elif violates_rule3(dir_1, dir_2, [m] + descendants_of(m,g), c):
                print '\t  Violates rule 3 at {}->{}<-{}'.format(s,m,t)
                for i in [m]+descendants_of(m,g): print '\t    Node: {}, in {}: {}'.format(i,c,i in c)
                return False
        
        print "\t  doesn't violate any rules!\n"
        return True

def corner_case (g, c, p):
    return True

# s->m->t or s<-m<-t where m is given
def violates_rule1 (d1, d2, inside):
    return d1 == d2 and inside

# s<-m->t where m is given
def violates_rule2 (d1, d2, inside):
    return d1 == 0 and d2 == 1 and inside

# s->m<-t where m is not given
def violates_rule3 (d1, d2, nodes, c):
    return d1 == 1 and d2 == 0 and not any([n in c for n in nodes])

def descendants_of (m,g):
    descendants = []
    frontier = [m]
    
    while len(frontier) > 0:
        node = frontier.pop(0)
        if node not in descendants: descendants.append(node)
        for new_node, edge in enumerate(g[node]):
            if edge == 0: continue
            if new_node in descendants or new_node in frontier: continue
            else: frontier.append(new_node)
    
    del descendants[0]
    return descendants
        
    
    

def sliding_window(seg, size):
    window = [seg[i:len(seg)-size+1+i] for i in xrange(size)]
    for values in zip(*window):
        yield values    

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 1:
        print 'Error: No input file given'
    else:
        print 'Error: too many inputs given'
