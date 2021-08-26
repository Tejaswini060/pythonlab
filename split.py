def split(arr,k):
    arr=arr[k:]+arr[:k]
    return arr
k=3
arr=[10,13,8,5,17,6]
print("output array is",split(arr,k))
