N = int(input("Enter an integer number "))

magic_array = [[0 for x in range(N)] for y in range(N)]

#pos 1
i = N - 1
j = N // 2

num = 1
while num <= N**2:
    if i == N:
        i = 0
    if j == N:
        j = 0
    
    if magic_array[i][j]:
        i = foo - 1
        j = boo
        continue
    else:
        magic_array[i][j] = num
        num = num + 1
    foo, boo = i , j
    i = i + 1
    j = j + 1
print(N)
for i in range(N):
    for j in range(N):
        print(magic_array[i][j], end="\t\t")
    print("")