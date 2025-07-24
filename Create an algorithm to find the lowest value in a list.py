my_array = [12,7, 9, 4, 11, 8]
minVal = my_array[0]
print(minVal)

for i in my_array:
  print(i,"<",minVal)
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)
print(my_array.min())