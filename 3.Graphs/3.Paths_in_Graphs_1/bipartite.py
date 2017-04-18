#Uses python3

import sys
import queue

color = []
dist = []

def bipartite(adj):
    #write your code here
    for i in range(len(adj)):
        dist.append(-999)
        color.append(-1)
    s = 0
    dist[s] = 0
    color[s] = 0
    queue = []
    queue.append(s)
    while len(queue) != 0:
        u = queue[0]
        queue.pop(0)
        for v in adj[u]:
            if dist[v] == -999:
                queue.append(v)
                dist[v] = dist[u] + 1
                color[v] = not color[u]
            else:
                if color[v] == color[u]:
                    return 0

    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
