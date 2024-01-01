
c = [12, 13, 14, 15, 16, 17, 18, 19]

result = []

for num in c:
    cube = num ** 3
    result.append((num, cube))


for t in result:
    print(t, end=" ")

