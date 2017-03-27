''' Program to find Nth root of any number and also give out as -1 if root of that nuber is in float'''

N=int(raw_input('enter value of n'))
M=int(raw_input('enter value of M'))
a=N
b=1.0/a
#print b

result=(M **b)
print result
if (result).is_integer():
    r=result/1.0
    print r
else:
    print -1
