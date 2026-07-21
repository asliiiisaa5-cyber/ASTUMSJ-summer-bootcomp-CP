t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    left = 1
    right = n - 1
    blue = [lst[0]]
    red = []
    while left < right:
        blue.append(lst[left])
        red.append(lst[right])
        if sum(red) > sum(blue) and len(red) < len(blue):
            print("YES")
            break
        left += 1
        right -= 1
    else:
        print("NO")
