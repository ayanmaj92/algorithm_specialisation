#Uses python3

import sys

visited = []

def explore(adj, x):
    #write your code here
    #print (adj)
    #print ("Visiting: ", x, y)
    visited.append(x)
    for w in adj[x]:
        if w not in visited:
            explore(adj, w)

def number_of_components(adj):
    result = 0
    #write your code here
    for i in range(len(adj)):
        if i not in visited:
            explore(adj, i)
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
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
