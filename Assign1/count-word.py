s1=input()
s1.strip()
l1=s1.split(' ')
print(l1)
i=0
wordcount=0
while i<len(l1):
    if l1[i]!='':
        wordcount+=1
    i+=1
print("total words",wordcount)        
print()