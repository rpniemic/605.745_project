# Greg Boss
# hw5 EN605.745

require(igraph)
require(abind)

# enter your graph using any igraph api
# ex (hw5). g=graph.formula(1-+2,1-+3,2-+3,2-+4,3-+4)

# ...or make a random DAG with a specified vertex count
# prob is likelihood one vertex is connected to another
#
rdag <- function(vertex_count,prob=.3) {
  u <- erdos.renyi.game(vertex_count, prob, directed=F)
  d <- as.directed(u)
 Ad <- get.adjacency(d)
  d <- graph.adjacency(Ad *(upper.tri(Ad) * 1))
  plot(d)
  d
}

# computes d-separation for a graph G, 
# between vertices Q,
# given evidence set E
#
dsep <- function(G,Q,E=vector()) {
	if(!is.dag(G)) stop("this algorithm works with directed graphs")
	if( any( E %in% Q ) ) stop("the query set cannot be in the evidence set")
	Ad = get.adjacency(G)
	U = as.undirected(G)
	Au = get.adjacency(U)

	evidence = classify_evidence(Ad,E,Q)
	ev_colliders=evidence[[1]]
	colliders=evidence[[2]]
	
	# TODO: combinations of verticies
	pair = Q

	# breadth first search for cycles
	paths = bfs_paths(Au,pair[1],pair[2],vector())

	for(k in 1:length(paths)) {
		
		# look for unblocked paths, one path at a time...
		path_is_blocked=FALSE
		path=paths[[k]]
		if( length(path) == 2) { plot_results( G,E,Q,"red" );return(FALSE) }

		if( any(colliders %in% path) ) {
			# are any of the vertices in the path potential colliders?
			for( collider in colliders[colliders %in% path] ) {

				if( is.collider_on_this_path( collider, path, Ad ) ) {
					path = path[! collider== path ]
					if( collider %in% ev_colliders ) {
						print(paste0("collider",collider))
						path_is_blocked=TRUE
						break # skip to checking blockers
					}
				}
			}	
		}
		# any blocker in the path qualifies this path
		if( ! path_is_blocked && any( E %in% path ) ) {
			print(paste("blockers",E[E %in% path]))
			path_is_blocked=TRUE
		}
		if(! path_is_blocked ) {
			plot_results( G, E, Q, "red")
			return(FALSE)	
		}
	}
	if( path_is_blocked )
	print("no unblocked paths")
	plot_results( G, E, Q, "green")
	return(TRUE)
}

# breadth-first-search for pathset
#
bfs_paths <- function(A, innode, target, visited, path_len=1) {
	if( path_len > nrow(A) || innode == target ) {return()}
	buf <- vector()
	visited = c( visited , innode )
	layer = subset(which(A[innode,]>0), !(which(A[innode,]>0) %in% visited))
	if( target %in% layer && path_len == 1 ) return( list( c( visited,target ) ) ) 
	for( node in layer) {
		if( node == target ) {
			new_path = c(visited,target)
			if( length(buf)==0 ) { buf = vector("list",1) }
			buf[length(buf)] = list(new_path)
		} else {
			buf = c( buf, bfs_paths( A,node,target,visited,path_len=1 ) )
		}
	}
	buf
}

# finds potential colliders
#
classify_evidence <- function(Ad,E,Q) {
	
	if( sum((lower.tri(Ad)*1)*Ad) > 0 ) {stop("first argument must be dag adjacency matrix")}
	if( length(E) >0 && max(E) > nrow(Ad) ) { stop("evidence nodes must be in the vertex set") }

	colliders <- vector()
	ev_colliders <- vector()
	
	# compute hop matrix set
	M=c(Ad);X=Ad;repeat { X = X %*% Ad; if( !sum(X) > 0 ) { break }; M=c(M,X) ; }
	
	# find all the colliders, and check those not in evidence set for descendents in the evidence set
	for(i in 1:ncol(Ad) ) { 
		if(sum(Ad[,i]) > 1 && ! i %in% Q ) {
			colliders <- c(colliders,i)
			for( A in M ) { 
				c = which(A[i,]>0)
				if( length(c) > 0 && c %in% E ) {
					ev_colliders <- c(ev_colliders,i)
					break 
				}
		    }
		}		
	}
	# blockers and colliders in the evidence set
	list(ev_colliders,colliders)
}

# qualifies colliders as on a path
#
is.collider_on_this_path <- function(e,path,Ad) {
	v1 = path[match(e,path)-1]
	v2 = path[match(e,path)+1]
	collider = FALSE
	if(sum(Ad[c(v1,v2),e])>1) {collider = TRUE}
	return(collider)
}

# plot
#
plot_results <- function(G,evidence,targets,color) {
	P=G # temp copy
	V(P)[targets]$color=color
	V(P)[evidence]$color="orange"
	plot(P,layout=layout.circle)
}
