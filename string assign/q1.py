s1=input()
# s1.strip()
l1=s1.split(' ')
print(l1)

j=-1

while j>=-(len(l1)):
    if l1[j]!='':
        
        print(l1[j],end=' ')  
    j-=1
      
print()