def hanoi(n,f,h,t):
        if n==0:
            return
        hanoi(n-1,f,t,h)
        print("Move disk",n,"from ",f,"to ",t)
        hanoi(n-1,h,f,t)

    n = int(input("Enter the number of disks "))
    hanoi(n,'A','B','c')
