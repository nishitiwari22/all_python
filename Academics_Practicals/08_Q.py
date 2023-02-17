# 8) Python program to check if the number is an Armstrong number or not


def armstrong():
   num = int(input("Enter any number: "))
   temp = num
   sum = 0
   count = 0
   while temp != 0:
      count = count + 1
      temp = int(temp/10)
   temp = num   
   while temp != 0:
      remainder = temp % 10
      p = 1
      for i in range(0, count):
         p = p*remainder
      
      sum = sum + p
      temp = int(temp/10)

   if sum == num:
      print(num, "is an Armstrong Number")
   else:
      print(num, " is not an Armstrong Number")

armstrong()


# Output:
# Enter any number: 153
# 153 is an Armstrong Number