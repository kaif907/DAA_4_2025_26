from typing import List
from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        
        for u, v, price in flights:
            graph[u].append((v, price))
        
        q = deque()
        q.append((src, 0, 0))
        
        dist = [float('inf')] * n
        dist[src] = 0
        
        while q:
            city, cost, stops = q.popleft()
            
            if stops > k:
                continue
            
            for next_city, price in graph[city]:
                new_cost = cost + price
                
                if new_cost < dist[next_city]:
                    dist[next_city] = new_cost
                    q.append((next_city, new_cost, stops + 1))
        
        return -1 if dist[dst] == float('inf') else dist[dst]
