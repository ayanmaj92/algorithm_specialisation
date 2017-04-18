#Uses python3
import sys
import math

'''UNION SET IMPLEMENTATION'''

class disjoint_set:
    def __init__(self, num):
        self.parent = [None]*num
        self.rank = [None]*num
        self.num_clusters = 0
    def make_set(self, i):
        self.parent[i] = i
        self.rank[i] = 0
        self.num_clusters = self.num_clusters + 1
    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def union_set(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
            self.num_clusters = self.num_clusters - 1
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] = self.rank[j_id] + 1
            self.num_clusters = self.num_clusters - 1

def calc_dist(x1, y1, x2, y2):
    #Calculate co-ordinate distance between two points
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

'''KRUSKAL'S ALGORITHM'''
def clustering(x, y, k):
    #write your code here
    tuple_nodes = []
    dist = -1.
    #Here we create the edges for all the nodes, then we sort it
    #We implement the list of nodes as a list of tuples containing
    #1st node, 2nd node, distance between them
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            tuple_nodes.append((i,j,calc_dist(x[i],y[i],x[j],y[j])))
    tuple_nodes.sort(key=lambda x:x[2])
    my_set = disjoint_set(len(x))
    #Create the sets from the vertices
    for i in range(len(x)):
        my_set.make_set(i)
    x_set = []
    #Keep a list of all the weights of the edges added to the MST
    list_dist = []
    #Iteration over all the edges
    for item in tuple_nodes:
        #If the two nodes don't belong to same set
        if my_set.find(item[0]) != my_set.find(item[1]):
            x_set.append(item[0])
            x_set.append(item[1])
            print ("Num clusters:",my_set.num_clusters)
            #Add the weight of the edge, also do UNION of the two sets
            list_dist.append((item[0],item[1],item[2]))
            my_set.union_set(item[0], item[1])
            '''
            We break at k-1 and not k. This is because when we again call union to join sets and
            get to k-1 clusters from k, we get to know the exact edge that is used. The edge that is
            chosen to join at this step is the distance between clusters at num_clusters=k.
            '''
            if my_set.num_clusters == k - 1:
                return list_dist[-1][2]
    
    return -1.


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
