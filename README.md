Smallest Connected Dominating Set Problem
=========================================

To run the greedy algorithm:
----------------------------

    python justgreed.py <name-of-graph> [algorithm]

The name-of-graph is the filename without the `.adjlist`. The algorithm is one
of the following

* null
* len
* oracle (default)

### nullHeuristic
Returns zero. 

### lenHeuristic
Returns the number of untouched nodes adjacent to the selected node

### oracleHeuristic
Returns the number of untouched nodes adjacent to the selected node, plus the
number of untouched nodes adjacent to its best child. 
