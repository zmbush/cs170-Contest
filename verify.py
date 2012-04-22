import solver
import graph
import sys
import copy

debugging = False

def verify(g, solution):
  if debugging: print "Copying graph"
  gcop = copy.deepcopy(g)
  for index in solution:
    if debugging: print "Removing node:",index
    gcop = graph.removeNode(gcop, index)
  if not gcop.graphEmpty():
    if debugging: print "Not Valid"
    return False
  if debugging: print "Determining if solution is connected"
  nextPossible = g[solution[0]]
  for index in solution[1:]:
    if index not in nextPossible:
      if debugging: print "Not Valid"
      return False
    nextPossible.update(g[index])
  if debugging: print "Valid"
  return True

if __name__ == "__main__":
  debugging = True
  if len(sys.argv) <= 1:
    print "You must specify an input file"
  else:
    g = graph.Graph(sys.argv[1] + '.adjlist')
    solution = solver.solve(g)
    if solution != None:
      verify(g, solution)
