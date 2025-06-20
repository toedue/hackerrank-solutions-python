n = int(input()) # 'n' representing the number of elements in the list
arr = map(int, input().split()) # Takes a line of space-separated numbers as input, splits them into strings,
                                 # maps each string to an int, creating a map object
array = list(arr) #Converts the map object into a list of integers
a = max(array) # Finds the maximum value in the list and stores it in variable 'a'
count = array.count(a) # Counts how many times the maximum value 'a' appears in the list
    
    
for i in range(count):  # Removes the maximum value from the list 'count' times
    array.remove(a)
    
b = max(array)
print(b)