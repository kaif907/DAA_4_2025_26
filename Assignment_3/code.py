# ================================
# 1. BINARY SEARCH
# ================================

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# Example
arr = [1, 3, 5, 7, 9, 11, 15]
print("Binary Search Result:", binary_search(arr, 7))


# ================================
# 2. SUBSET SUM (DECISION VERSION)
# ================================

def subset_sum(arr, target):
    n = len(arr)

    for i in range(1 << n):  # 2^n subsets
        current_sum = 0

        for j in range(n):
            if i & (1 << j):
                current_sum += arr[j]

        if current_sum == target:
            return True

    return False


# Example
arr2 = [3, 4, 5, 2]
print("Subset Sum (Decision):", subset_sum(arr2, 9))


# ================================
# 3. SUBSET SUM (VERIFICATION VERSION)
# ================================

def verify_subset(subset, target):
    total = 0

    for num in subset:
        total += num

    return total == target


# Example
subset = [4, 5]
print("Subset Sum (Verification):", verify_subset(subset, 9))


# ================================
# 4. TRAVELING SALESMAN PROBLEM (BRUTE FORCE)
# ================================

import itertools

def tsp(graph):
    n = len(graph)
    vertices = list(range(1, n))
    min_path = float('inf')

    for perm in itertools.permutations(vertices):
        current_cost = 0
        k = 0

        for j in perm:
            current_cost += graph[k][j]
            k = j

        current_cost += graph[k][0]
        min_path = min(min_path, current_cost)

    return min_path


# Example Graph
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("TSP Minimum Cost:", tsp(graph))


# ================================
# OPTIONAL: PERFORMANCE MEASUREMENT
# ================================

import time

# Binary Search Performance
arr_large = list(range(1, 1000000))
start = time.time()
binary_search(arr_large, 999999)
end = time.time()
print("Binary Search Time:", end - start)


# Subset Sum Performance
arr_small = [1, 2, 3, 4, 5, 6]
start = time.time()
subset_sum(arr_small, 10)
end = time.time()
print("Subset Sum Time:", end - start)


# TSP Performance
start = time.time()
tsp(graph)
end = time.time()
print("TSP Time:", end - start)
