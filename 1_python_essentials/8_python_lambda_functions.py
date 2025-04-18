# python lambda function

# lambda functions are anonymous functions, we use lambda keyword to define an
# unnamed function, we cannot control statement with lambda functions

# syntax : lambda arguments: expression
print("* lambda functions")
add = lambda x,y: x + y
print("lambda add:",add(10,20))

square = lambda x: x**2
print("lambda square:",square(12))

# common uses
# 1.map() takes an iterable and applies the function to every item in it
# and return an iterator of the result
# 2.filter() takes iterable and filter it based on condition where it is true

# 1.map()
print("\n* using map()")
nums = [1,2,3,4,5]
square = list(map(lambda x: x**2,nums))
print(square)

# 2.filter()
print("\n* using filter()")
nums = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x: x % 2 == 0,nums))
print(even)
