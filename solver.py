import graph
import sys
import copy

debugging = False

def solve(g, heuristic=len):
  if debugging: print "Graph input:",g
  g = copy.deepcopy(g)
  ans = []
  bestChoice = -1
  bestScore = -1
  i = 0
  for adjacent in g:
    if heuristic(adjacent) > bestScore:
      bestChoice = i
      bestScore = heuristic(adjacent)
    i += 1

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
      if heuristic(g[choice]) > bestScore:
        bestChoice = choice
        bestScore = heuristic(g[choice])

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
