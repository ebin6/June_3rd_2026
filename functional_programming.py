numbers=[34,27,12,4,89]



n=list(filter(lambda num:num%2==0,numbers))
print(n)

from functools import reduce

total=reduce(lambda a,b:a+b,numbers)
print(total)