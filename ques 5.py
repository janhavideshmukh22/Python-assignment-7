n=int(input("Enter number of inputs:"))
l=[]
for i in range(0,n):
    s=int(input("Enter number:"))
    l.append(s)
l.sort()
print(l)

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
 
x=int(input("Enter value to be searched:"))
result = binary_search(l, x)
print("Number of occurences:",l.count(x))
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
