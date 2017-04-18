# python3
import sys

#Implements the Better BW Matching using Count_symbol and First_Occurence maps.

def PreprocessBWT(bwt):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  # Implement this function yourself
  pass
  starts = {}
  occ_counts_before = {}
  chars = set(bwt)
  first_col = sorted(list(bwt))
  for c in chars:
    starts[c] = first_col.index(c)
  #print (starts)
  for i in range(len(bwt)+1):
    if i == 0:
      for c in chars:
        occ_counts_before[c] = [0]
    else:
      for c in chars:
        '''if not c in occ_counts_before:
          if bwt[i] == c:
            occ_counts_before[c] = [1]
          else:
            occ_counts_before[c] = [0]'''
        #else:
        if bwt[i-1] == c:
          occ_counts_before[c].append(occ_counts_before[c][-1] + 1)
        else:
          occ_counts_before[c].append(occ_counts_before[c][-1])
  #print (occ_counts_before)
  return starts, occ_counts_before


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  # Implement this function yourself
  top = 0
  bottom = len(bwt) - 1

  while top <= bottom:
    if len(pattern) != 0:
      symbol = pattern[-1]
      pattern = pattern[:-1]
      #print (pattern)
      if symbol in bwt[top:bottom+1]:
        top = starts[symbol] + occ_counts_before[symbol][top]
        bottom = starts[symbol] + occ_counts_before[symbol][bottom+1]-1
      else:
        return 0
    else:
      #print (top," ",bottom)
      return bottom-top+1
     


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).  
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))
