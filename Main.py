from typing import List
def selectionSort(array, size) -> List[int]:
for index in range(size):
min = index
Selection and Insertion Sorting
for j in range(index+1,size):
if array[j]<array[min]:
min = j
(array[min],array[index]) = (array[index],array[min])
return array

input_data = input()
data = []
for item in input_data.split(', '):
if item.isnumeric():
data.append(int(item))
elif item.lstrip("-").isnumeric():
data.append(int(item))
print(selectionSort(data, len(data)))

