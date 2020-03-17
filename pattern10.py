def pa(k):
    #k=int(input("Enter the number : "))
    for a in range (0,k-1):
        for b in range (0,k-1-a):
            print(" ",end="")
        for c in range (0,a+1):
            print("* ",end="")
        print(" ")
    for i in range (0,k):
        for j in range (0,i):
            print(" ",end="")
        for z in range(0,k-i):
            print("* ",end="")
        print(" ")

pa(5)
