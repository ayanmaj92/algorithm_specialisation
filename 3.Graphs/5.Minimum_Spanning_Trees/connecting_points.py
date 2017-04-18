#Uses python3
import sys
import math

'''IMPLEMENTING MIN_HEAP'''
class MinHeap:
	def __init__(self):
		#heap array is where we store the nodes in heap
		'''Each element in the heap will be a list, the 0th element
		will be the node id, the 1th element will be the current 
		weight associated with it.
		'''
		self.heap = []
		'''
		We also implement a dictionary, which basically maps the node-id
		to the particular heap index. If the node-id is removed from the heap,
		we make the dict value -1 to indicate it is no longer there.
		'''
		self.mapper = {}

	def parent(self, i):
		return math.floor((i - 1) / 2)

	def left_child(self, i):
		return (2*i + 1)

	def right_child(self, i):
		return (2*i + 2)

	def sift_up(self,i):
		
		while i > 0 and self.heap[self.parent(i)][1] > self.heap[i][1]:
			
			self.mapper[self.heap[i][0]] = self.parent(i)
			self.mapper[self.heap[self.parent(i)][0]] = i
			
			self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
			i = self.parent(i)

	def sift_down(self,i):
		minIndex = i
		lc = self.left_child(i)
		if lc < len(self.heap) and self.heap[lc][1] < self.heap[minIndex][1]:
			minIndex = lc
		rc = self.right_child(i)
		if rc < len(self.heap) and self.heap[rc][1] < self.heap[minIndex][1]:
			minIndex = rc
		if i != minIndex:
			self.mapper[self.heap[i][0]] = minIndex
			self.mapper[self.heap[minIndex][0]] = i
			self.heap[i], self.heap[minIndex] = self.heap[minIndex], self.heap[i]
			self.sift_down(minIndex)

	def insert(self,p):
		self.heap.append(p)
		self.mapper[p[0]] = len(self.heap) - 1
		self.sift_up(len(self.heap) - 1)

	def extract_min(self):
		res = self.heap[0]
		self.heap[0] = self.heap[len(self.heap) - 1]
		self.mapper[self.heap[0][0]] = 0
		self.heap.pop()
		self.mapper[res[0]] = -1
		self.sift_down(0)
		return res

	def remove(self,i):
		self.heap[i][1] = -(sys.maxsize)
		self.sift_up(i)
		self.extract_min()

	def change_priority(self, z, p):
		i = self.mapper[z]

		old_p = self.heap[i][1]
		self.heap[i][1] = p
		if p > old_p:
			self.sift_down(i)
		else:
			self.sift_up(i)

def calc_dist(x1, y1, x2, y2):
	#Calculate co-ordinate distance between two points
	return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

'''PRIM'S ALGORITHM'''
def minimum_distance(x, y):
    result = 0.
    #Initialize cost and parent lists
    cost = [sys.maxsize]*(len(x))
    parent = [None]*(len(x))
    #We start from node-0
    cost[0] = 0
    #Initialize heap and insert the vertices into it
    h = MinHeap()
    for i in range(len(x)):
    	h.insert([i, cost[i]])
    #Start iteration
    while len(h.heap) != 0:
    	v = h.extract_min()
    	#Here we go through all the other points given other than the current point
    	#This is because we can theoretically connect any city to any other city directly
    	for i in range(len(x)):
    		if i != v[0]:
    			#Calculate the distance which becomes the weight of the edge
    			weight = calc_dist(x[v[0]], y[v[0]], x[i], y[i])
    			if h.mapper[i] != -1 and cost[i] > weight:
    				cost[i] = weight
    				parent[i] = v
    				h.change_priority(i, cost[i])
    #print (cost)
    #Whatever cost is calculated for each node, adding them will give us the total cost
    result = sum(cost)
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
