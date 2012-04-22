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
  """
  graph = []
  for n in range(nodes):
    node = []
    for edge in range(degree):
      while True:
        val = random.randrange(nodes)
        if val != n and val not in node:
          if val > n or n not in graph[val]:
            node.append(val)
            break
    graph.append(node)
  
  for i in range(nodes):
    print i,' '.join(str(x) for x in graph[i])
  """
