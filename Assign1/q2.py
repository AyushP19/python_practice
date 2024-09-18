l1 = ["java", 76, 765, "Reactnative", "javascript", "python"]

for e in l1.copy():
    if type(e) != int:
        l1.remove(e)

print(l1)