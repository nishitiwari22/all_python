# import seaborn as sns
# from matplotlib import pyplot as plt

# fmri = sns.load_database("fmri")
# fmri.head()

# sns.lineplot(x="timepoint", y="signal", data=fmri)
# plt.show()

# fmri.shape

# sns.lineplot(x="timepoint", y="signal", data=fmri)
# plt.show()


# print("Enter num 1")
# num1 = input()
# print("Enter num 2")
# num2 = input()
# try:
#     print("The sum of these 2 numbers is" , 
#         int(num1)+int (num2))
# except Exception as e:
#     print(e)


f = open("nisi.txt", "rt")
# f = open("lists.py")
# content = f.read()

# print(f.readline())
# print(f.readline())
# print(f.readline())

print(f.readline())  # It will print the lines with the '\n'


for line in f:
    print(line, end="")   #Don't use content = f.read() otherwise this loop won't work

# print(content)

# content = f.read(344)
# print("1", content)

# content = f.read(34445)
# print("2", content)

f.close()
