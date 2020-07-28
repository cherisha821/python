list1 = []  
n = int(input("Enter the number of elements in a list : ")) 
  
for i in range(0, n): 
    element = int(input()) 
  
    list1.append(element)
      
print(list1)
for num in list1: 
      
    # checking condition 
    if num >= 0: 
       print(num,end= " ")
