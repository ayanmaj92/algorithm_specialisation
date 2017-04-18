#Uses python3

import sys

visited = {}
exp = []
def explore(adj, x):
	#write your code here
	visited[x] = 1
	for w in adj[x]:
		if visited[w] == 0:
			explore(adj, w)
	exp.insert(0, x)

#def dfs(adj, used, order, x):

def dfs(adj):
	#write your code here
	for i in range(len(adj)):
		if visited[i] == 0:
			explore(adj, i)


def toposort(adj):
	used = [0] * len(adj)
	order = []
	dfs(adj)
	#write your code here
	#exp.reverse()
	order = exp
	#order = list(visited.reverse())
	return order

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
	order = toposort(adj)
	for x in order:
		print(x + 1, end=' ')

