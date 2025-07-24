a = lambda x , y: x+ y
print(a(50,10))

def lambdafun(x):
    return lambda a: a+x
one = lambdafun(5)
two = lambdafun(5)
print(one(10))
print(two(50))


