##!!!!!!!!!!! THIS QUESTION IS NOT DONE, READ EMAIL FROM TA
# part a
def lucas(n):
	a,b = 2,1
	if n < 0:
		print("please enter a vaild number")
	elif n == 0:
		return a
	elif n == 1:
		return b
	else:
		for i in range(2, n + 1):
			a, b = b, a + b
		return b

def cal_lucas(n):
    i=0
    while i < n:
        print(lucas(i), end=' ')
        i=i+1
    #print()

#cal_lucas(21)
