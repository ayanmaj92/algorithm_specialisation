# python3
import sys

def BWT(text):
	list1 = []
	for i in range(len(text)):
		text = text[1:] + text[0]
		list1.append(text)
	list1.sort()
	bwt = ""
	for i in range(len(list1)):
		bwt += list1[i][-1]
	return bwt

if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	print(BWT(text))