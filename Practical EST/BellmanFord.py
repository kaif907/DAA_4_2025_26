V=5

edges=[
(0,1,-1),
(0,2,4),
(1,2,3),
(1,3,2),
(1,4,2),
(3,2,5),
(3,1,1),
(4,3,-3)
]

def bellman_ford(src):

    dist=[float('inf')]*V

    dist[src]=0

    # Relax edges V-1 times
    for i in range(V-1):

        for u,v,w in edges:

            if dist[u] != float('inf') and \
               dist[u]+w < dist[v]:

                dist[v]=dist[u]+w

    # Check negative cycle
    for u,v,w in edges:

        if dist[u] != float('inf') and \
           dist[u]+w < dist[v]:

            print("Negative Cycle Found")
            return

    print(dist)

bellman_ford(0)
