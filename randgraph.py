import sys
import random

if len(sys.argv) <= 2:
  print "Argument Required"
else:
  nodes = 0
  degree = 0
  try:
    nodes = int(sys.argv[1])
    degree = int(sys.argv[2])
  except ValueError:
    print "You must specify an integer"
    sys.exit(-1)

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
  
