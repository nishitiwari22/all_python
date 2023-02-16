
a = "Hey I am Nishi Nishi Nishi"
b = "Nishi"
c = "blah"
# print (a[15])
# s = a[0:]
# print(s)

count = a.count(b)
print(count)
count = a.count(c)
print(count)
count = a.find(b) 
# Agar mil jaate hai string toh uska index return karta hai
print(count)
c = a[count:]
print(c)
a = a.replace(" ","-")
print(a)

d = "chomu"
count = a.find(d) 
# Agar nhi hai wo string uss index mai toh -1 return hoga
print(count)

# if(a.find(b)>=0):
#     print("Yes")
# else:
#     print("No")

# Above is the current logic

if(b in a):
    print("Yes")
else:
    print("No")
    
for c in a:
    print(c)
    
a = a.upper()
print(a)

b = b.lower()
print(b)