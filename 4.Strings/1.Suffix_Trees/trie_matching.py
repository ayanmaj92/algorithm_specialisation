# python3
import sys

NA = -1

numNodes = -1

class Node:
	def __init__ (self):
		#self.next = [NA] * 4
		self.next = {}
def build_trie(patterns):
	global numNodes
	#tree = dict()
	# write your code here
	#tree[0] = {}
	tree = Node()
	numNodes = numNodes + 1
	for pattern in patterns:
		#currentNode = tree[0]
		currentNode = tree
		for i in range(len(pattern)):
			currentSymbol = pattern[i]
			if currentSymbol in currentNode.next:
				#currentNode = tree[currentNode[currentSymbol]]
				currentNode = currentNode.next[currentSymbol]
			else:
				numNodes = numNodes + 1
				#tree[numNodes] = {}
				#newNode = tree[numNodes]
				newNode = Node()
				currentNode.next[currentSymbol] = newNode
				#currentNode[currentSymbol] = numNodes
				currentNode = newNode
	return tree
def prefix_trie_match(text, trie):
	j = 0
	symbol = text[j]
	v = trie
	while 1:
		#print(v)
		if len(v.next) == 0:
			return True
		elif symbol in v.next:
			v = v.next[symbol]#trie[v[symbol]]
			if j < len(text) - 1:
				j = j + 1
				symbol = text[j]
			else:
				symbol = None
		else:
			return False


def solve (text, n, patterns):
	result = []
	#write your code here
	trie = build_trie(patterns)
	#print (trie)
	for i in range(len(text)):
		if prefix_trie_match(text[i:], trie):
			result.append(i)
		#print (result)
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
