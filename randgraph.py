import sys
import random
import networkx as nx

if len(sys.argv) <= 3:
  print "Argument Required"
else:
  nodes = 0
  degree = 0
  fname = sys.argv[1]
  try:
    nodes = int(sys.argv[2])
    degree = float(sys.argv[3])
  except ValueError:
    print "You must specify an integer"
    sys.exit(-1)
  print nodes
  print degree
  G = nx.fast_gnp_random_graph(nodes, degree)
  nx.write_adjlist(G, fname) 
