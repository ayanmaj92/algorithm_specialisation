#Uses python3

import sys

sys.setrecursionlimit(200000)

visited = {}
visited_rev = {}
exp = []


'''These functions are for exploring
the given graph'''
def explore(adj, x):
	#write your code here
	visited[x] = 1
	for w in adj[x]:
		if visited[w] == 0:
			explore(adj, w)
	exp.insert(0, x)

def dfs(adj):
	#write your code here
	for i in range(len(adj)):
		if visited[i] == 0:
			explore(adj, i)

'''These functions are for exploring
the reversed graph'''
def explore_rev(adj_rev, x):
	#write your code here
	visited_rev[x] = 1
	for w in adj_rev[x]:
		if visited_rev[w] == 0:
			explore_rev(adj_rev, w)
	exp.insert(0, x)

def dfs_rev(adj_rev):
	#write your code here
	for i in range(len(adj_rev)):
		if visited_rev[i] == 0:
			explore_rev(adj_rev, i)



def number_of_strongly_connected_components(adj):
	result = 0
	#write your code here
	'''Construct the adjacency list for
	the reversed graph'''
	adj_rev = [[] for _ in range(len(adj))]
	for i in range(len(adj)):
		for item in adj[i]:
			adj_rev[item].append(i)
	#Traverse the reverse graph to obtain reverse post order
	dfs_rev(adj_rev)
	
	for v in exp:
		if visited[v] == 0:
			explore(adj, v)
			result = result + 1
	return result

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
	adj = [[] for _ in range(n)]
	for (a, b) in edges:
		adj[a - 1].append(b - 1)
	for i in range(n):
		visited[i] = 0
	for i in range(n):
		visited_rev[i] = 0
	print(number_of_strongly_connected_components(adj))
