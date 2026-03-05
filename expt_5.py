arr = list(map(int, input("Enter the array elements: ").split()))
num = len(arr)
target_S = int(input("Enter the target Sum: "))

dp = [[0]*(target_S+1) for _ in range(num+1)]

for i in range(num+1):
    dp[i][0] = 1

for i in range(1, num+1):
    for j in range(1, target_S+1):
        if arr[i-1] <= j:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
        else:
            dp[i][j] = dp[i-1][j]

print(dp[num][target_S])
