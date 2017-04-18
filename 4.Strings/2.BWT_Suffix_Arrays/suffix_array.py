# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  result = []
  # Implement this function yourself
  suffix_map = {}
  for i in range(len(text)):
    suffix_map[text[i:]] = i
  keys = list(suffix_map.keys())
  keys.sort()
  for k in keys:
    result.append(suffix_map[k])
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
