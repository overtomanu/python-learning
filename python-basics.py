# strings, comma prints space
print("Hello" , "world")

# int and float
print(42 , 3.1416)

# list
print([5,3,4,1])

# set, 2 is printed only once
print({2,3,2})

# map
print({"k1":"v1",3:54,"k1":"v2"})

# tuple
print(("string value",5,3,4,1))

# pyright gives error as type annotation is declared for str but int value is assigned
# code executes fine though
programming_language: str = 'Python'
programming_language=1
print(programming_language)

# lambda functions in python
def square(num):
    return num**2

my_nums = [1,2,3,4,5]

print(map(square,my_nums))