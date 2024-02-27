n = int(input())
m = int(input())
city_to_index = {}
distance = [[float('inf')] * n for i in range(n)]
for i in range(m):
    c1, c2, path = input().split()
    path = int(path)
    if c1 not in city_to_index:
        city_to_index[c1] = len(city_to_index)
    if c2 not in city_to_index:
        city_to_index[c2] = len(city_to_index)
    c1_index = city_to_index.get(c1)
    c2_index = city_to_index.get(c2)
    distance[c1_index][c2_index] = path
    distance[c2_index][c1_index] = path
for i in range(n):
    for u in range(n):
        for v in range(n):
            distance[u][v] = min(distance[u][v], distance[u][i] + distance[i][v])
c1, c2 = input().split()
c1_index = city_to_index.get(c1)
c2_index = city_to_index.get(c2)
if c1 == c2:
    print(0)
else:
    print(distance[c1_index][c2_index])
