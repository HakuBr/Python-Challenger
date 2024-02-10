# Dada uma matriz ordenada de inteiros distintos e um valor alvo, retorne o
# índice se o alvo for encontrado. Caso contrário, retorne o índice onde
# estaria se fosse inserido na ordem.
# Você deve escrever um algoritmo com complexidade de tempo de execução O(log n).
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

import time
import numpy as np

def search_insert_position(nums,target):
  start = time.time()
  if target in nums:
    print(nums.index(target))
  else:
    nums.append(target)
    nums_sorted = sorted(nums)
  end = time.time()
  print(round(np.log(len(nums))/(end-start)))
  return nums_sorted.index(target)




search_insert_position([1,3,5,6],7)