
b=100

def test():
    print("inside test ", b)
    b=19
    print("inside test but b is reintitialized", b)

print("outside test fucntion ", b)

def main():
    for a in range(15,45,1):
        print("inside main but b not reinitized inside main ", b)
        for b in range(2,a+1,1):
            if(a%b==0):
                break 
            print("b inside main and reintialized ", b)  
            if(a==b):
                print(a)
    print("inside main outside inner for", b)

print(b)

if __name__ == main():
    main()
    test()