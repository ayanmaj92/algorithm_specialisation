#Uses python3

import sys
import queue
import heapq as hq

def distance(adj, cost, s, t):
	#write your code here
	dist = []
	prev = []
	#print (adj)
	#print (cost)
	for i in range(len(adj)):
		dist.append(sys.maxsize)
		#prev.append(None)
	dist[s] = 0
	#print ("Initial:", dist)
	queue = []
	for i in range(len(adj)):
		hq.heappush(queue, (dist[i], i))
	#print (queue)
	while len(queue) != 0:
		ind = hq.heappop(queue)
		u = ind[1]
		for v in range(len(adj[u])):
			#print (u, v)
			if dist[adj[u][v]] > (dist[u] + cost[u][v]):
				dist[adj[u][v]] = dist[u] + cost[u][v]
				hq.heappush(queue, (dist[adj[u][v]], adj[u][v]))
	#print ("Final: ", dist[t])
	if dist[t] < sys.maxsize:
		return dist[t]
	return -1


if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
	data = data[3 * m:]
	adj = [[] for _ in range(n)]
	cost = [[] for _ in range(n)]
	for ((a, b), w) in edges:
		adj[a - 1].append(b - 1)
		cost[a - 1].append(w)
	s, t = data[0] - 1, data[1] - 1
	print(distance(adj, cost, s, t))
