# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def dynamic_weight(W, w):
	result = 0
	value = [(len(w) + 1)*[0] for i in range(W + 1)]
	for i in range(len(w)):
		for weight in range(1,W + 1):
			#print("value[",weight,"][",i+1,"] =")
			value[weight][i + 1] = value[weight][i]
			if w[i] <= weight:
				val = value[weight - w[i]][i] + w[i]
				if val > value[weight][i + 1]:
					#print("value[",weight,"][",i+1,"] =")
					value[weight][i + 1] = val
	#print(value)
	return value[W][len(w)]
	


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(dynamic_weight(W, w))
