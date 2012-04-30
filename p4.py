from solver import solve
from verify import verify
from justgreed import *

import networkx as nx

import solver
import sys
import os

if __name__ == "__main__":
  if len(sys.argv) <= 1:
    print "You must specify a directory"
    sys.exit(1)
  heur = "oracle"

  output = file("hw13_4", 'w')

  if len(sys.argv) > 2:
    heur = sys.argv[2]
  directory = sys.argv[1]
  if directory[-1] != '/':
    directory += '/'
  for f in os.listdir(directory):
    if ".translated" in f: continue
    if ".adjlist" not in f: continue
    
    g = nx.read_adjlist(directory + f)
    print "Solving:", f, "with", heur+"Heuristic"

    solution = solve(g, heuristic=eval(heur + "Heuristic"), alg="greedy")
    


    if solution != None:
      print " => Size of solution:",len(solution)
      print " => Solution:",' '.join(solution)    
      print >> output, f, " ".join(solution)
    else:
      print >> output, f
      print " => No Solution!"


