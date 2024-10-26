def plusMinus(arr):
    postive=0
    negative=0
    zero=0
    for i in arr:
        if i >0:
            postive+=1
        elif i <0:
            negative+=1
        else:
            zero+=1
    n=len(arr)
    pos_ratio= postive/n
    neg_ratio= negative/n
    zero_ratio= zero/n
    
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")
    
           
    
n = 6
arr = [-4, 3, -9, 0, 4, 1]

# Call the function
plusMinus(arr)