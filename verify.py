import solver
import graph
import sys
import copy

def verify(g, solution):
  gcop = copy.deepcopy(g)
  for index in solution:
    gcop = graph.removeNode(gcop, index)
  if not gcop.graphEmpty():
    return False
  nextPossible = g[solution[0]]
  for index in solution[1:]:
    if index not in nextPossible:
      return False
    nextPossible.update(g[index])
  return True

if __name__ == "__main__":
  if len(sys.argv) <= 1:
    print "You must specify an input file"
  else:
    g = graph.Graph(sys.argv[1] + '.adjlist')
    solution = solver.solve(g)
    print "Graph:",g
    print "Solution:",solution
    if solution != None:
      if verify(g, solution):
        print "Solution Verified!"
      else:
        print "Solution invalid!!!"
    else:
      print "No Solution found"
