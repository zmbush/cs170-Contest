from solver import solve
from verify import verify

import networkx as nx
import solver
import sys

"""
The worst solution. 
"""
def nullHeuristic(g, node, touched):
  return 0

"""
Very basic greedy algorithm
"""
def lenHeuristic(g, node, touched):
  untouched = [l for l in g.neighbors(node) if l not in touched] 
  return len(untouched)

"""
Greedy with one turn look-ahead
"""
def oracleHeuristic(g, node, touched):
  untouched = [l for l in g.neighbors(node) if l not in touched]
  score = len(untouched)
  maxAdd = 0
  for neighbor in untouched:
    u = [l for l in g.neighbors(neighbor) if l not in touched]
    maxAdd = max(maxAdd, (len(u) - 1) * 0.5)
  score += maxAdd
  return score

if __name__ == "__main__":
  if len(sys.argv) <= 1:
    print "Input graph required"
  else:
    heur = "oracle"
    if len(sys.argv) > 2:
      heur = sys.argv[2]
    """Read Graph in"""
    g = nx.read_adjlist('graphs/' + sys.argv[1] + '.adjlist')
    print "Solving", sys.argv[1], "with", heur+"Heuristic"

    """Solve For Graph with greedy algorithm"""
    solution = solve(g, heuristic=eval(heur + "Heuristic"), alg="greedy")
    print "Size of solution:",len(solution)
    print "Solution:",solution

    """Verify the correctness of the solution"""
    if verify(g, solution):
      print "Valid!"
    else:
      print "Invalid"
