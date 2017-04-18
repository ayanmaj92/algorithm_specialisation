# python3
import sys

def countSort(arr):
 
	# The output character array that will have sorted arr
	output = [0 for i in range(4)]
 
	# Create a count array to store count of inidividul
	# characters and initialize count array as 0
	count = [0 for i in range(4)]
 
	# For storing the resulting answer since the 
	# string is immutable
	ans = ["" for _ in arr]
 
	# Store count of each character
	for i in arr:
		count[ord(i)] += 1
 
	# Change count[i] so that count[i] now contains actual
	# position of this character in output array
	for i in range(4):
		count[i] += count[i-1]
 
	# Build the output character array
	for i in range(len(arr)):
		output[count[ord(arr[i])]-1] = arr[i]
		count[ord(arr[i])] -= 1
 
	# Copy the output array to arr, so that arr now
	# contains sorted characters
	for i in range(len(arr)):
		ans[i] = output[i]
	return ans 

def InverseBWT(bwt):
	# write your code here
	fc = list(bwt)
	fc.sort()
	#first_column = "".join(fc)
	#print(first_column)
	lc_map = {}
	fc_map = {}
	lc = list(bwt)
	for i in range(len(bwt)):
		if not bwt[i] in lc_map:
			lc_map[bwt[i]] = 1
		else:
			lc_map[bwt[i]] += 1
		lc[i] += str(lc_map[bwt[i]])

		if not fc[i] in fc_map:
			fc_map[fc[i]] = 1
		else:
			fc_map[fc[i]] += 1
		fc[i] += str(fc_map[fc[i]])
	
	#print(lc)		
	#print(fc)
	rec = "$"
	i = 0
	rec += lc[i][0]
	while(1):
		i = fc.index(lc[i])
		if (lc[i][0] == "$"):
			break
		rec += lc[i][0]
	return rec[::-1]


if __name__ == '__main__':
	#bwt = sys.stdin.readline().strip()
	bwt = "A$"
	for i in range(3):
		bwt += "G"
	print (bwt)
	print(InverseBWT(bwt))
	print("Done")