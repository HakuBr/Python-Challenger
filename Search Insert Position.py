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