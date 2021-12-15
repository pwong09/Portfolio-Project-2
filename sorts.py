import random

def quicksort(list, start, end, comparison_function):
  if start >= end:
    return
  pivot_idx = random.randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  less_than_pointer = start
  for i in range(start, end):
    if comparison_function(pivot_element, list[i]):
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  quicksort(list, start, less_than_pointer - 1, comparison_function)
  quicksort(list, less_than_pointer + 1, end, comparison_function)

def bubblesort(list):
  iteration_count = 0
  for i in range(len(list)):
    for index in range(len(list) - i - 1):
      iteration_count += 1
      if list[index] > list[index + 1]:
        list[index], list[index + 1] = list[index + 1], list[index]
  return list

