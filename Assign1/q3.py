# a="ayush"
# print(a)


# for a in range(15,45,1):
#    for b in range(2,a+1,1):
#       if(a%b==0):
#          break 
#    print("b is ", b)  
#    if(a==b):
#       print(a)
# print(b)

# fac=1
# n = int(input("Enter a number"))
# for a in range(1,n+1,1):
#     fac =fac*a
# print(fac)


# sum=0
# n = int(input())
# while n!=0:
#     temp=n%10
#     n=n/10
#     int(sum) =sum+temp
# print(sum)

# n = int(input())
# while n!=0:
#    a=n%2
#    print(a)
#    n=n//2



# n = int(input("ENTER A NUMBE - "))
# while n !=0:
#  a = n%10
#  print(a , end="")
#  n = int(n/10)


# i,j=2,2
# for a in range(i,100,1):
#    # b=j
#    for b in range(j,a+1,1):
#       if(a%b==0):
#          break  
#    if(a==b):
#       print(a)

# i, j = 2, 2
# for a in range(i, 100, 1):
#     for b in range(2,a,1):
#         if a % b == 0:
#             break
#     else:
#         print(a)

# l1 = ['java','python','c','dotnet','reacnative', 'sql']
# l1.append('dbms')
# print(l1)


# firstlist = ["Java", "Python", "SQL"]
# secondlist = ["C", "Cpp", "NoSQL"] 
# for item in secondlist: 
#  firstlist.append(item)
# print(firstlist)

# n = int(input("enter  a number: "))
# list1=[]
# # thislist = ["java","sql","C","Reactnative","javascript","python"]
# for i in range(0,n):
#     list1[i]= input()
# print(list1)    

# n = int(input('enter a number: '))
# l1=[297,55,536,325,346,435,366,999,8,642]
# # for i in range(l1):
# l1.sort()
# print(l1[-1])

# n = int(input("How many numbers you want to enter"))
# print("Enter", n, "numebrs")
# l1=[]
# i,sum=0,0
# while i<n:
#     l1.append(int(input()))
#     i+=1
# for i in l1:
#    sum =sum +i
# print(sum)        




# n = int(input("How many number you want to enter"))

l1 = ["java", 76, 765, "Reactnative", "javascript", "python"]

for e in l1.copy():
    if type(e) != int:
        l1.remove(e)

print(l1)

