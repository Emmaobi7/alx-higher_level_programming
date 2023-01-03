square = []
for x in range(10):
    square.append(x**2)
print(square)

sq = list(map(lambda x: x**2, range(10)))
print(sq)

su = [x**2 for x in range(10)]
print(su)

print()
print()



matrix = [
        [2,3,4,5],
        [1,2,3,4],
        [2,4,6,8],
        ]
d2 = [[row[i] for row in matrix] for i in range(4)]
print(d2)

transpose = []
for i in range(4):
    transpose.append([row[i] for row in matrix])
print(transpose)
