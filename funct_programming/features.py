#map, filter, zip and reduce
from functools import reduce
def multiply_by2(item):
    return item * 2
#map
print( list(map(multiply_by2 ,[1,2,3])) )

def check_odd(item):
    return item % 2 != 0
#filter
print( list(filter(check_odd ,[1,2,3])) )

#zip
print( list(zip([1,2,3], [10,20,30])) )


#reduce
def accumulator(acc,item):
    return acc + item
print( reduce(accumulator ,[1,2,3],0) )
