# f = open("vipnotes.txt")
# content = f.read()
# print(content)

# f.close()

f = open ("vipnotes.txt", "rt")
content = f.read()
print(content)

content = f.read(3455)
print("l", content)

content = f.read(3455)
print("2", content)
f.close()