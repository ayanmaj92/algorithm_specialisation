# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def sequence_finder(n):
	sequence = []
	min_ops = 0*[n]
	#sequence.append(1)
	min_ops.append(0)
	if n > 1:
		for i in range(2,n + 1):
			list1 = []
			temp_max = a = b = c = sys.maxsize
			list1.append(temp_max)
			if i % 3 == 0:
				a = min_ops[(i // 3) - 1] + 1
				list1.append(a)
			if i % 2 == 0:
				b = min_ops[(i // 2) - 1] + 1
				list1.append(b)
			c = min_ops[i - 1 - 1] + 1
			list1.append(c)
			x = min(list1)
			min_ops.append(x)
	#print(min_ops)
	#print(min_ops[-1])
	#print(min_ops[32077])
	#print(len(min_ops))
	i = n
	while i > 0:
		ops = min_ops[i - 1]
		sequence.append(i)
		if i % 3 == 0 and min_ops[(i // 3) - 1] == ops - 1:
			i = i // 3
		elif i % 2 == 0 and min_ops[(i // 2) - 1] == ops - 1:
			i = i // 2
		else:
			i = i - 1
	#print(sequence)
	return reversed(sequence)



input = sys.stdin.read()
n = int(input)
sequence = list(sequence_finder(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
