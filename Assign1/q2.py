# l1 = ["java", 76, 765, "Reactnative", "javascript", "python"]

# for e in l1.copy():
#     if type(e) != int:
#         l1.remove(e)

# print(l1)
# a = input("enter a character")
# count=0
# for s in input("ENTER A STRING"):
#     if s=='a' or s=='e' or s=='i' or s=='o' or s=='u':
#       count=count+1       
# print(count)

# s = input("enter string")
# s.strip()
# l1=s.split(' ')
# print(l1)

# count=0
# s = input("Enter a string")
# for e in s:
#     if e in e>='a' and e<='z' or e>='A' and e<='Z':
#         count=count+1
# print(count)        

  

# string = "     This      ayu        is a sample string        with   multiple     words      "
string = input()
words = string.split()

word_count = len(words)

print("Number of words:", word_count)