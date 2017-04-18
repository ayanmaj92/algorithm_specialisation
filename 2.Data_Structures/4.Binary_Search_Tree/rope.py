# python3

import sys

from sys import stdin

# Splay tree implementation
count = 0
# Vertex of a splay tree
class Vertex:
  def __init__(self, key, data, sum, left, right, parent):
    (self.key, self.data, self.sum, self.left, self.right, self.parent) = (key, data, sum, left, right, parent)

# Updates key of node, updates the size
def update(v):
	if v == None:
		return
	v.sum = (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0) + 1
	if v.left != None:
		v.left.parent = v
	if v.right != None:
		v.right.parent = v
# Small Rotation
def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else:
      grandparent.right = v
# Calls Zig-Zig, Zig-Zag
def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  else:
    # Zig-zag
    smallRotation(v);
    smallRotation(v);

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.

def find(root, key):
	v = root
	last = root
	next = None
	while v != None:
		sm1 = v.left.sum if v.left != None else 0
		if v.sum < key:
			break
		if sm1 + 1 == key:
			last = v
			next = v
			break
		if (sm1 + 1) > key:
			v = v.left
		else:
			v = v.right
			key = key - sm1 - 1
	root = splay(last)
	return (next, root)
# Splits tree based on a key
def split(root, key):
	(result, root) = find(root, key+1)
	if result == None:
		return (root, None)
	right = splay(result)
	left = right.left
	right.left = None
	if left != None:
		left.parent = None
	update(left)
	update(right)
	return (left, right)

# Merge left and right trees
def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right

root = None

# Inorder Traversal of the Tree
def inorder (p):
	res = ""
	key_do = 0
	if p == None:
		return
	temp = []
	current = p

	while len(temp) != 0 or current is not None:
		pass
		if current is not None:
			temp.append(current)
			current = current.left
		else:
			if len(temp) != 0:
				res = res + temp[-1].data
				current = temp[-1].right
				temp.pop()
	return res
# Inserts new node into the tree
def insert(x,c):
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if right == None or right.key != x:
    new_vertex = Vertex(x, c, x, None, None, None)
  root = merge(merge(left, new_vertex), right)
  update(root)
# Define the class Rope
class Rope:
	def __init__(self, s):
		self.s = s
		self.s1 = s
		for i in range(len(s)):
			insert(i, s[i])
	def result(self):
		self.s = inorder(root)
		return self.s
	
	def result1(self):
		return self.s1

	'''def process_naive(self, i, j, k):
    	# Write your code here
		t = self.s1[0:i] + self.s1[j+1:]
		self.s1 = t[0:k] + self.s1[i:j + 1] + t[k:]
	'''
	# Main processing of the node
	def process(self, i, j, k):
		global root
		# Split the entire tree into 3 parts: left, middle part from i to j, and right
		(left, middle) = split(root, i)
		(middle, right) = split(middle, j - i + 1)
		
		t, r = None, None
		# Boundary case: when k has max value
		if k == len(self.s) - (j - i + 1):
			root = merge(left, merge(right, middle))
		# Boundary case: when k is same as i
		elif k == i:
			root = merge(merge(left, middle), right)
		elif k != 0:
			flag = 0
			if k >= j: #when the destination is more than the right limit
				(v1, v2) = split(right, k - j + middle.sum - 1)
				root = merge(left, merge(v1, merge(middle, v2)))
			elif k < i: #when the destination is less than the left limit
				(v1, v2) = split(left, k)
				root = merge(merge(v1, merge(middle, v2)), right)
			elif k > i and k < j: #when the destination is in between left and right limits
				(v1, v2) = split(right, k - i)
				root = merge(left, merge(v1, merge(middle, v2)))
		else:
			root = merge(merge(middle, left), right)


rope = Rope(sys.stdin.readline().strip())

q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
print(rope.result())
