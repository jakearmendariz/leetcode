def longest_range(arr):
    group = set(arr)
    longest = 0
    while len(group) > 0:
        n = group.pop()
        bottom,top = n,n
        while True:
            if n-1 in group:
                bottom = n-1
                n-=1
                group.remove(n)
            else:
                break
        while True:
            if n+1 in group:
                top = n+1
                n+=1
                group.remove(n)
            else:
                break
        if top - bottom > longest:
            longest = top - bottom
    return longest

arr = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(longest_range(arr))
