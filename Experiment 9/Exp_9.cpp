class Solution {
public:

    int minDifference(vector<int>& arr) {

        int n = arr.size();

        int totalSum = 0;

        for(int x : arr)
            totalSum += x;

        vector<vector<bool>> dp(n+1, vector<bool>(totalSum+1,false));

        for(int i=0;i<=n;i++)
            dp[i][0] = true;

        for(int i=1;i<=n;i++) {

            for(int j=1;j<=totalSum;j++) {

                if(arr[i-1] <= j)
                    dp[i][j] = dp[i-1][j] || dp[i-1][j-arr[i-1]];
                else
                    dp[i][j] = dp[i-1][j];
            }
        }

        int minDiff = totalSum;

        for(int s1=0;s1<=totalSum/2;s1++) {

            if(dp[n][s1]) {
                minDiff = min(minDiff, totalSum-(2*s1));
            }
        }

        return minDiff;
    }
};
