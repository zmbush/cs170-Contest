from graph import Graph
from solver import solve
from verify import verify
import sys

def nullHeuristic(g, node):
  return 0

def lenHeuristic(g, node):
  return len(g[node])

def heu(g, node):
  print "Evaluating for node:",node
  adjacent = g[node]
  score = len(adjacent)
  print "Score so far:",score
  maxAdd = 0
  for neighbor in adjacent:
    print "\tChecking neighbor:",neighbor
    maxAdd = max(maxAdd, len(g[neighbor]) - 1)
    print "maxAdd is now:",maxAdd
  score += maxAdd
  print "Final Score:",score
  print
  return score

if __name__ == "__main__":
  if len(sys.argv) <= 1:
    print "Input graph required"
  else:
    heur = "heu"
    if len(sys.argv) > 2:
      heur = sys.argv[2]
    g = Graph(sys.argv[1] + ".adjlist")
    solution = solve(g, heuristic=eval(heur), alg="greedy")
    print "Size of solution:",len(solution)
    print "Solution:",solution
    if verify(g, solution):
      print "Valid!"
    else:
      print "Invalid"
