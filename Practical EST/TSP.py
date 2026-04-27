from itertools import permutations

graph=[
[0,10,15],
[10,0,20],
[15,20,0]
]

cities=[1,2]

ans=float('inf')

for p in permutations(cities):

    cost=0
    k=0

    for j in p:
        cost += graph[k][j]
        k=j

    cost += graph[k][0]

    ans=min(ans,cost)

print(ans)
