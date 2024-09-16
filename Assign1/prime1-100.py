i,j=2,2
for a in range(i,100,1):
   # b=j
   for b in range(j,a+1,1):
      if(a%b==0):
         break  
   if(a==b):
      print(a)