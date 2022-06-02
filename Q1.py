def lucas(n):
    if n < 0:
        print("Please enter a number greater than 0.")
    elif n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

def cal_lucas(n):
    lucas_num = lucas(1)
    i = 1
    while lucas_num < n:
        print(lucas_num, end=' ') 
        i += 1
        lucas_num = lucas(i)
    #print()

#cal_lucas(5)