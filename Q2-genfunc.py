# part b
def lucas(n):
	a, b = 2, 1
	for i in range(n):
	    yield a
	    a, b = b, a + b

def cal_lucas(n):
    #print(list(lucas(n)))
    for num in lucas(n):
        print(num, end=' ')

#cal_lucas(20)