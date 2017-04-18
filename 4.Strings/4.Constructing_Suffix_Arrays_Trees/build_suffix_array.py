# python3
import sys
maps = {"A":1,"T":4,"G":3,"C":2,"$":0}
def sort_characters(string):
  order = [-1] * len(string)
  count = [0, 0, 0, 0, 0]

  for i in range(len(string)):
    count[maps[string[i]]] = count[maps[string[i]]] + 1
  #print (count)
  for j in range(1, 5):
    count[j] = count[j] + count[j - 1]
  #print (count)
  for i in range(len(string)-1,-1,-1):
    c = string[i]
    #print (c)
    count[maps[c]] = count[maps[c]] - 1
    #print (count[maps[c]])
    order[count[maps[c]]] = i
    #print (order)
  #print (order)
  return order

def compute_char_classes(string, order):
  arr_class = [-1] * len(string)
  arr_class[order[0]] = 0
  for i in range(1, len(string)):
    if string[order[i]] != string[order[i-1]]:
      arr_class[order[i]] = arr_class[order[i-1]] + 1
    else:
      arr_class[order[i]] = arr_class[order[i - 1]]
  return arr_class

def sort_doubled(string, l, order, arr_class):
  count = [0] * len(string)
  new_order = [-1] * len(string)
  for i in range(len(string)):
    count[arr_class[i]] = count[arr_class[i]] + 1
  for j in range(1, len(string)):
    count[j] = count[j] + count[j - 1]
  for i in range(len(string)-1,-1,-1):
    start = (order[i] - l + len(string)) % len(string)
    cl = arr_class[start]
    count[cl] = count[cl] - 1
    new_order[count[cl]] = start
  return new_order

def update_classes(new_order, arr_class, l):
  n = len(new_order)
  new_class = [-1] * n
  new_class[new_order[0]] = 0
  for i in range(1, n):
    cur = new_order[i]
    prev = new_order[i-1]
    mid, mid_prev = (cur + l) % n, (prev + l) % n
    if (arr_class[cur] != arr_class[prev]) or (arr_class[mid] != arr_class[mid_prev]):
      new_class[cur] = new_class[prev] + 1
    else:
      new_class[cur] = new_class[prev]
  return new_class

def build_suffix_array(text):
  #print ('Called')
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  '''result = []'''
  # Implement this function yourself
  order = sort_characters(text)
  class_array = compute_char_classes(text, order)
  l = 1
  while l < len(text):
    order = sort_doubled(text, l, order, class_array)
    class_array = update_classes(order, class_array, l)
    l = 2 * l
    #print (l)
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
