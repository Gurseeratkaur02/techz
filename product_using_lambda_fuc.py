from functools import reduce
l=[5,6,1,3,2]
print(l)
product=reduce((lambda x,y:x*y),l)
print('the product is:',product)
