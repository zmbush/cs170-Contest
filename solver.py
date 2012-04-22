import graph
import sys
import copy

debugging = False

def solve(g, heuristic=lambda g, node: len(g[node]), alg="greedy"):
  return eval(alg)(g, heuristic)

def greedy(g, heuristic):
  if debugging: print "Graph input:",g
  g = copy.deepcopy(g)
  ans = []
  bestChoice = -1
  bestScore = -1
  for node in range(len(g)):
    h = heuristic(g, node)
    if h > bestScore:
      bestChoice = node
      bestScore = h

  if debugging: print "chosing node:", bestChoice
  possibleNextChoices = g[bestChoice]
  if debugging: print "connected next choices:",possibleNextChoices
  ans.append(bestChoice)

  g.removeNode(bestChoice)
  if debugging: print "Graph after removing choice:",g

  while not g.graphEmpty():
    bestChoice = -1
    bestScore = -1
    if len(possibleNextChoices) == 0:
      return None
    for choice in possibleNextChoices:
      h = heuristic(g, choice)
      if h > bestScore:
        bestChoice = choice
        bestScore = h

    if debugging: print "chosing node:",bestChoice
    possibleNextChoices.remove(bestChoice)
    ans.append(bestChoice)
    possibleNextChoices.update(g[bestChoice])
    if debugging: print "connected next choices:",possibleNextChoices

    g.removeNode(bestChoice)
    if debugging: print "Graph after removing choice:",g
  return ans
  
if __name__ == "__main__":
  debugging = True
  if len(sys.argv) <= 1:
    print "You must specify an input file"
  else:
    g = graph.Graph(sys.argv[1] + '.adjlist')
    print solve(g)
