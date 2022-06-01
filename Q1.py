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
    i = 0
    while i <= n: 
        i = i+1
        print(lucas(i), end =' ')
    print()