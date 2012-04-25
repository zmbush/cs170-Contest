# from graph import Graph
from solver import solve
import solver
from verify import verify
import networkx as nx
import sys

def nullHeuristic(g, node, touched):
  return 0

def lenHeuristic(g, node, touched):
  untouched = [l for l in g.neighbors(node) if l not in touched] 
  return len(untouched)

def oracleHeuristic(g, node, touched):
  # print "Evaluating for node:",node
  untouched = [l for l in g.neighbors(node) if l not in touched]
  score = len(untouched)
  # print "Score so far:",score
  maxAdd = 0
  for neighbor in untouched:
    # print "\tChecking neighbor:",neighbor
    # score += (len(g[neighbor]) - 1)*.01
    u = [l for l in g.neighbors(neighbor) if l not in touched]
    maxAdd = max(maxAdd, (len(u) - 1) * 0.5)
    # print "maxAdd is now:",maxAdd
  score += maxAdd
  # print "Final Score:",score
  # print
  return score

if __name__ == "__main__":
  if len(sys.argv) <= 1:
    print "Input graph required"
  else:
    heur = "oracle"
    if len(sys.argv) > 2:
      heur = sys.argv[2]
    g = nx.read_adjlist(sys.argv[1] + '.adjlist')
    print "Solving", sys.argv[1], "with", heur+"Heuristic"
    solution = solve(g, heuristic=eval(heur + "Heuristic"), alg="greedy")
    print "Size of solution:",len(solution)
    print "Solution:",solution
    if verify(g, solution):
      print "Valid!"
    else:
      print "Invalid"
