# 10) Python program to remove punctuation from string.

# initializing string
test_str = "My name ! #Minhaj Khan $% and I am studying *BCA;"

# printing original string
print("The original string is : " + test_str)

# initializing punctuations string
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Removing punctuations in string
# Using loop + punctuation string
for ele in test_str:
    if ele in punctuation:
        test_str = test_str.replace(ele, "")

# printing result
print("The string after punctuation filter : " + test_str)