#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

'''
TrieConstruction(Patterns)
Trie ← a graph consisting of a single node root
for each string Pattern in Patterns:
	currentNode ← root
	for 𝑖 from 0 to |Pattern| − 1:
		currentSymbol ← Pattern[𝑖]
		if there is an outgoing edge from currentNode with label currentSymbol:
			currentNode ← ending node of this edge
		else:
			add a new node newNode to Trie
			add a new edge from currentNode to newNode with label currentSymbol
			currentNode ← newNode
return Trie
'''
numNodes = -1
def build_trie(patterns):
	global numNodes
	tree = dict()
	# write your code here
	tree[0] = {}
	numNodes = numNodes + 1
	for pattern in patterns:
		currentNode = tree[0]
		for i in range(len(pattern)):
			currentSymbol = pattern[i]
			if currentSymbol in currentNode:
				currentNode = tree[currentNode[currentSymbol]]
			else:
				numNodes = numNodes + 1
				tree[numNodes] = {}
				newNode = tree[numNodes]
				currentNode[currentSymbol] = numNodes
				currentNode = newNode
	return tree


if __name__ == '__main__':
	patterns = sys.stdin.read().split()[1:]
	tree = build_trie(patterns)
	#print (tree)
	for node in tree:
		for c in tree[node]:
			print("{}->{}:{}".format(node, tree[node][c], c))
