N = int(input("Enter an integer number "))
array = []
for i in range(N):
    col = []
    for j in range(N):
        foo = int(input(f"Enter an integer number between 0-{N**2} "))
        col.append(foo)
    array.append(col)

magic = 0

i = 0
for x in array:
    sum = 0
    i += 1
    for y in x:
        sum += y
    if sum == N*(N**2 + 1)/2:
        print(f"ROW {i} YES")
    else:
        print(f"ROW {i} NO")
        magic += 1
i = 0
while i < N:
    sum = 0
    for x in range(N):
        sum += array[x][i]
    if sum == N*(N**2 + 1)/2:
        print(f"COLUMN {i+1} YES")
    else:
        print(f"COLUMN {i+1} NO")
        magic += 1
    i += 1

diag1 = 0
diag2 = 0
for i in range(N):
    for j in range(N):
        if i == j:
            diag1 += array[i][j]
        if i + j == N - 1:
            diag2 += array[i][j]
if diag1 == N*(N**2 + 1)/2:
    print("DIAG1 YES")
else:
    print("DIAG1 NO")
    magic += 1
if diag2 == N*(N**2 + 1)/2:
    print("DIAG2 YES")
else:
    print("DIAG2 NO")
    magic += 1


check_array = []
for i in array:
    check_array.extend(i)
if len(set(check_array)) == len(check_array):
    print("UNIQUE YES")
else:
    print("UNIQUE NO")
    magic += 1

if magic == 0:
    print("MAGIC YES")
else:
    print("MAGIC NO")
