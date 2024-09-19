# i=1
# whi le i<=3:
#     n = int(input("enter no."))
#     if(n%2==0):
#      print("WINNER") 
#      i=i+1 
#     else: 
#        print("LOOSE") 

# if(i==4):
    # print("LOOSE")  

#METHOD TO SOLVE IN LESS LINE
s2="1a2b3c4"
a=sum([ int(e) for e in s2 if ord(e)>=49  and ord(e)<57])
print(a)