def findMedian(arr):
    # Write your code here
    sorted_lst = sorted(arr)
    # Return the middle element
    median = sorted_lst[len(sorted_lst) // 2]
    return median


arr=[0,1,2,4,6,5,3]
res=findMedian(arr)
print(res)