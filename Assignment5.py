list1 = list(range(1,100))
  
res3= list(filter(lambda x: (x % 3 == 0), list1)) 
res5= list(filter(lambda x: (x % 5 == 0), list1)) 
  
print(res3,"These numbers are only divisible by 3 between 1-100 number \n") 
print(res5,"These numbers are only divisible by 5 between 1-100 number ")