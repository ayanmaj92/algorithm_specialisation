#Uses python3

import sys

visited = []
flag = 0
#index = 0

temp_list = [] #this list is to track the path we are taking. 
#When returning from the recursion for a particular vertex, we pop it as we are no longer
#following that path.
def explore(adj, x):
	global flag, temp_list, visited
	#temp_list = []
	#write your code here
	#print (adj)
	#print ("Visiting: ", x, y)
	'''print ("Visiting: ", x)
	print ("visited list: ", visited, "\ntemp: ", temp_list)'''
	visited.append(x)
	temp_list.append(x) #here we add that vertex to our path
	for w in adj[x]:
		if w in temp_list: #check whether the vertex at end of this edge is already on the path we are going on
			flag = 1
		if w not in visited:
			explore(adj, w)
	temp_list.pop() #we are done following this path upto this point. So the last vertex is to be popped as it is all explored


def acyclic(adj):
	global flag, index, visited
	for i in range(len(adj)):
		#print ("Iteration")
		if i not in visited:
			explore(adj, i)
		index = len(visited)
		if flag == 1:
			return 1
	return 0

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
	adj = [[] for _ in range(n)]
	for (a, b) in edges:
		adj[a - 1].append(b - 1)
	#print (adj)
	print(acyclic(adj))
