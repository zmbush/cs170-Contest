import graph
import sys

if __name__ == "__main__":
  if len(sys.argv) <= 1:
    print "Require filename"
  else:
    g = graph.Graph(sys.argv[1] + '.adjlist')
    out = open(sys.argv[1] + ".dot", 'w')
    print >> out, "graph {"
    for node in range(len(g)):
      for child in g[node]:
        print >> out, "   ",node,"--",child
      g.removeNode(node)
    print >> out, "}"
