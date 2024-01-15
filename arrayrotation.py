arr = [1, 2, 3, 4, 5];     
    
n = 1;    # how many times array should be shifted
   
print("Original array: ");    
for i in range(0, len(arr)):    # displaying the first or real array
    print(arr[i]),     
     
for i in range(0, n):    # rotate the element of array using for loop 
    
    first = arr[0];    # saving the first element to a variable
        
    for j in range(0, len(arr)-1):    
        arr[j] = arr[j+1];    #shifting to left by one             
  
    arr[len(arr)-1] = first;    # adding the first element to array from the variable
     
print();    
     

print("Array after left rotation: ");    
for i in range(0, len(arr)):    
    print(arr[i])
