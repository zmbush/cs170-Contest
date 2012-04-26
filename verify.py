import copy
import graph
import solver
import sys

import networkx as nx

debugging = False

def verify(g, solution):
  if debugging: print "Copying graph"
  gcop = copy.deepcopy(g)
  touched = set()
  for index in solution:
    if debugging: print "Removing node:",index
    touched.add(index)
    touched.update(gcop.neighbors(index))
    gcop.remove_node(index)
  if len(touched) != len(g.nodes()):
    if debugging: print "Not Valid"
    return False
  if debugging: print "Determining if solution is connected"
  nextPossible = set(g.neighbors(solution[0]))
  for index in solution[1:]:
    if index not in nextPossible:
      if debugging: print "Not Valid"
      return False
    nextPossible.update(g.neighbors(index))
  if debugging: print "Valid"
  return True

if __name__ == "__main__":
  debugging = True
  if len(sys.argv) <= 1:
    print "You must specify an input file"
  else:
    G = nx.read_adjlist('graphs/' + sys.argv[1] + '.adjlist')
    solution = solver.solve(G)
    if solution != None:
      verify(G, solution)
