from array import *

# create array and traverse

my_arr = array('i',[1, 2, 3, 4, 5])

print('Step 1')
for i in my_arr:
    print(i)


# Acces through indexes
print('Step 2')
print(my_arr[0])


# Append value to array 
print('Step 3')
my_arr.append(6)
print(my_arr)


# Inset value with insert
print('Step 4')
my_arr.insert(6, 7)
print(my_arr)


# Extend array with extend()
print('Step 5')
my_arr2 = array('i', [10, 11, 12])
my_arr.extend(my_arr2)
print(my_arr)


# Add item from list into array fromList()
print('Step 6')
temp_list = [20, 21, 22]
my_arr.fromlist(temp_list)
print(my_arr)


# Remove from array with remove()
print('Step 7')
my_arr.remove(1)
print(my_arr)


# Remove from array with pop()
print('Step 8')
my_arr.pop()
print(my_arr)


# Fetch any element through its index using index()
print('Step 9')
print(my_arr.index(21))


# Reverse array with reverse()
print('Step 10')
my_arr.reverse()
print(my_arr)


# Get array buffer with buffer_info()
print('Step 11')
print(my_arr.buffer_info())


# Check for amount of recurring numbers in array
print('Step 12')
my_arr.append(2)
print(my_arr.count(2))


# Convert array to string with tostring()
# Append a string to char with fromstring()
print('Step 13')
str_arr = my_arr.tostring()
print(str_arr)

ints = array('i')
ints.fromstring(str_arr)
print(ints)


# Array to python list with tolist()
print('Step 14')
# print(my_arr.tolist())


# Slice elements from array
print('Step 15')
print(my_arr[1:4])
