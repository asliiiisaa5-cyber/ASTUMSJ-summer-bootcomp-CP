n = int(input())
for i in range(n):
    t = int(input())
    lst = list(map(int,input().split()))
    gap = max(lst)-min(lst)
    numofop = (gap+1)//2
    print(numofop)
