import sys

debugging = False

class Graph:
  def __init__(self, filename):
    f = open(filename)
    graph = {}
    for line in f:
      if debugging: print "Reading line:",line
      txt = [int(t) for t in line.strip().split()]
      start = txt[0]
      for end in txt[1:]:
        if debugging: print "Adding",start,'->',end
        if start in graph:
          graph[start].add(end)
        else:
          graph[start] = set([end])
        if debugging: print "Adding",end,'->',start
        if end in graph:
          graph[end].add(start)
        else:
          graph[end] = set([start])
    self.graph = list(graph.values())
  
  def removeNode(self, node):
    for adj in self.graph:
      if adj != None:
        if node in adj:
          adj.remove(node)
    self.graph[node] = None

  def graphEmpty(self):
    for adj in self.graph:
      if adj != None and len(adj) > 0:
        return False
    return True

  def __str__(self):
    return str(self.graph)

  def __iter__(self):
    return iter(self.graph)

  def __getitem__(self, i):
    return self.graph[i]

  def __setitem__(self, i, value):
    self.graph[i] = value

def loadGraph(filename):
  f = open(filename)
  graph = {}
  for line in f:
    if debugging: print "Reading line:",line
    txt = [int(t) for t in line.strip().split()]
    start = txt[0]
    for end in txt[1:]:
      if debugging: print "Adding",start,'->',end
      if start in graph:
        graph[start].add(end)
      else:
        graph[start] = set([end])
      if debugging: print "Adding",end,'->',start
      if end in graph:
        graph[end].add(start)
      else:
        graph[end] = set([start])
  return list(graph.values())

def removeNode(graph, node):
  for adj in graph:
    if adj != None:
      if node in adj:
        adj.remove(node)
  graph[node] = None
  return graph

def graphEmpty(graph):
  for adj in graph:
    if adj != None and len(adj) > 0:
      return False
  return True

if __name__ == "__main__":
  debugging = True
  if len(sys.argv) <= 1:
    print "You must specify an input file"
  else:
    graph = Graph(sys.argv[1] + '.adjlist')
    print graph
