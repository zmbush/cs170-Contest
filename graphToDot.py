import graph
import sys
import networkx as nx

if __name__ == "__main__":
  if len(sys.argv) <= 1:
    print "Require filename"
  else:
    G = nx.read_adjlist('graphs/' + sys.argv[1] + '.adjlist')
    nx.write_dot(G, sys.argv[1] + '.dot')
