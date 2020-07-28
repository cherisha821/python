#fibonacci
n = int(input("Enter the number of terms you want? "))
n1= 0
n2 = 1
count = 0

if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto 1 is :")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       n3 = n1 + n2
       # update values
       n1 = n2
       n2 = n3
       count += 1
