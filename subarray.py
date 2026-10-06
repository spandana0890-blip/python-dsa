def min_subarray_with_sum(arr, target):
  min_length = float('inf')
  window_sum = 0
  start = 0
  
  for end in range(len(arr)):
      window_sum += arr[end]
      
      while window_sum >= target:
          min_length = min(min_length, end - start + 1)
          window_sum -= arr[start]
          start += 1
  
  return min_length if min_length != float('inf') else 0
numbers=[2,3,1,2,4,3]
print(min_subarray_with_sum(numbers,7))