# # F Strings
# # Embed Python expressions or variables inside of a string wihtout concatenation or string formatting or any other method user may use
# name = 'Nishi'
# print(f'Hello {name} { 2+3 }')

# x = (f'Hello {name} { 2+3 }')
# print(x)
# # Both can be used

# Unpacking
# Allows you to do is assigned variables to all of the values inside of some type of collection in PYTHON 
tup = (1,2,3,4,5)
lst = [1,2,3,4,5]
string = "hello"
dic = {"a" : 1, "b": 2}
coords = [4,5]

a,b,c,d,e = string
print(a,b,c,d,e)

a,b = dic.items()
print(a,b)

x,y = coords
print(x,y)