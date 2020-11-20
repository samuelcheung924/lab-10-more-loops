def hanoi(n,source,helper,target):
        if n==0:
            return
        hanoi(n-1,source,target,helper)
        print("Move disk",n,"from ",source,"to ",target)
        hanoi(n-1,helper,source,target)

n = int(input("Enter the number of disks\n"))
hanoi(n,'A','B','C')
