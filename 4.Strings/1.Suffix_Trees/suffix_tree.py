# python3
import sys

nl = []
class SuffixTree(object):
	
	class Node(object):
		def __init__(self, lab):
			self.label = lab
			self.out = {}
	def __init__(self, st):
		#st += '$'
		#self.count = 0
		self.root = self.Node(None)
		self.root.out[st[0]] = self.Node(st)
		if not self.root.out[st[0]] in nl:
			nl.append(self.root.out[st[0]])
		#self.count += 1
		# add the rest of the text...

		for i in range(1, len(st)):
			#print ("Processing: "+st[i])
			cur = self.root
			j = i
			while j < len(st):
				if st[j] in cur.out:
					child = cur.out[st[j]]
					lab = child.label
					k = j + 1
					while k-j < len(lab) and st[k] == lab[k-j]:
						k += 1
					if k-j == len(lab):
						cur = child
						j = k
					else:
						cExist, cNew = lab[k-j], st[k]
						mid = self.Node(lab[:k-j])
						#self.count += 1
						if not mid in nl:
							nl.append(mid)
						mid.out[cNew] = self.Node(st[k:])
						#self.count += 1
						if not mid.out[cNew] in nl:
							nl.append(mid.out[cNew])
						mid.out[cExist] = child
						child.label = lab[k-j:]
						cur.out[st[j]] = mid
						break
				else:
					#print ("Hitting else for: "+st[j])
					cur.out[st[j]] = self.Node(st[j:])
					#self.count += 1
					if not cur.out[st[j]] in nl:
						nl.append(cur.out[st[j]])

def build_suffix_tree(text):
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
  result = []
  # Implement this function yourself
  stree = SuffixTree(text)
  #print (len(nl))
  for node in nl:
  	result.append(node.label)
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))