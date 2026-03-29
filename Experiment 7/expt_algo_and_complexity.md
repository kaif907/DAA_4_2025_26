1.First I create a graph using adjacency list from given flights.

2.Then I use a queue to apply BFS traversal.

3.Each queue element stores:

(i)current city

(ii)cost till now

(iii)number of stops used

4.Start from source city with cost = 0.

5.Traverse neighbors:

(i)update cost if cheaper

(ii)push into queue with stops + 1

6.If stops exceed K, ignore that path.

7.Finally return minimum cost if reachable, else -1.

**Time Complexity:** O(K * E)
 (because we traverse edges up to K levels)

**Space Complexity:** O(N + E)
 (for graph + queue)
