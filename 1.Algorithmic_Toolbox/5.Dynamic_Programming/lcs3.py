#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here
    LCS = [[[0]*(len(c)+1) for x in range(len(b)+1)] for x in range(len(a)+1)]
    for i in range(1,len(a)+1):
    	for j in range(1,len(b)+1):
    		for k in range(1,len(c)+1):
    			if a[i-1] == b[j-1] == c[k-1]:
    				LCS[i][j][k] = LCS[i-1][j-1][k-1] + 1
    			else:
    				LCS[i][j][k] = max([LCS[i-1][j][k],LCS[i][j-1][k],LCS[i][j][k-1],
    					LCS[i-1][j-1][k],LCS[i-1][j][k-1],LCS[i][j-1][k-1]])
    return LCS[len(a)][len(b)][len(c)]

def lcs2(a, b):
	LCS = [[0]*(len(b)+1) for x in range(len(a)+1)]
	for i in range(1,len(a)+1):
		for j in range(1,len(b)+1):
			if a[i-1] == b[j-1]:
				LCS[i][j] = LCS[i-1][j-1] + 1
			else:
				LCS[i][j] = max([LCS[i-1][j],LCS[i][j-1]])
	return LCS[len(a)][len(b)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
