# from graph import Graph
from solver import solve
from verify import verify
import networkx as nx
import sys

def nullHeuristic(g, node):
  return 0

def lenHeuristic(g, node):
  return len(g.neighbors(node))

def oracleHeuristic(g, node):
  # print "Evaluating for node:",node
  adjacent = g.neighbors(node)
  score = len(adjacent)
  # print "Score so far:",score
  maxAdd = 0
  for neighbor in adjacent:
    # print "\tChecking neighbor:",neighbor
    # score += (len(g[neighbor]) - 1)*.01
    maxAdd = max(maxAdd, (len(g.neighbors(neighbor)) - 1) * 0.5)
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
