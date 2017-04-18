#Uses python3

import sys
import queue

def bfs(adj, q):
	#write your code here
	last_visit = []
	last_dist = []
	#for i in range(len(adj)):
	#	last_dist.append(-999)
	#dist[s] = 0
	queue = []
	queue = queue + q
	flags = [0]*len(adj)
	for i in queue:
		flags[i] = 1
	#print ("Relaxed:",queue)
	last_visit = last_visit + q
	while len(queue) != 0:
		u = queue[0]
		queue.pop(0)
		#print ("Current:",u)
		for v in adj[u]:
			#print ("Current Edge:",v)
			'''
			if v not in last_visit:
				queue.append(v) ##Add unvisited to the queue to process
				last_visit.append(v)
			'''
			if flags[v] != 1:
				queue.append(v)
				last_visit.append(v)
				flags[v] = 1
	#print (last_visit)
	return last_visit

def shortet_paths(adj, cost, s, distance, reachable, shortest):
	#write your code here
	dist = []
	prev = []
	#print (adj)
	#print (cost)
	set_a = []
	
	for i in range(len(adj)):
		dist.append(sys.maxsize)
	dist[s] = 0
	distance[s] = 0
	for i in range(len(adj)):
		for u in range(len(adj)):
			for v in range(len(adj[u])):
				#Relax edge
				if not (dist[adj[u][v]] == sys.maxsize and dist[u] == sys.maxsize):
					if dist[adj[u][v]] > (dist[u] + cost[u][v]):
						##print ("Here:", u, v)
						##print (dist,"::",cost)
						dist[adj[u][v]] = dist[u] + cost[u][v]
						distance[adj[u][v]] = dist[adj[u][v]]
						if i == len(adj) - 1:
							if u not in set_a:
								set_a.append(u)
							if adj[u][v] not in set_a:
								set_a.append(adj[u][v])
	pass
	##print ("Dist: ", dist)
	set_a = bfs(adj, set_a)
	for i in range(len(dist)):
		if dist[i] != sys.maxsize:
			reachable[i] = 1
	for i in set_a:
		if dist[i] != sys.maxsize:
			shortest[i] = 0
	


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
	s = data[0]
	s -= 1
	distance = [10**19] * n
	reachable = [0] * n
	shortest = [1] * n
	##print ("ADJ: ", adj)
	shortet_paths(adj, cost, s, distance, reachable, shortest)
	for x in range(n):
		if reachable[x] == 0:
			print('*')
		elif shortest[x] == 0:
			print('-')
		else:
			print(distance[x])

