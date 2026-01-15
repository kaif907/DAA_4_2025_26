#include <bits/stdc++.h>
using namespace std;

long long operations = 0;
int maxDepth = 0;

void complexRec(int n, int depth = 1) {

    maxDepth = max(maxDepth, depth);

    if (n <= 2) {
        operations++;
        return;
    }

    int p = n;
    while (p > 0) {
        vector<int> temp(n);
        for (int i = 0; i < n; i++) {
            operations++;
            temp[i] = i ^ p;
        }
        p >>= 1;
    }

    vector<int> small(n);
    for (int i = 0; i < n; i++) {
        operations++;
        small[i] = i * i;
    }

    reverse(small.begin(), small.end());

    complexRec(n / 2, depth + 1);
    complexRec(n / 2, depth + 1);
    complexRec(n / 2, depth + 1);
}

int main() {
    int n;
    cin >> n;

    auto start = chrono::high_resolution_clock::now();

    complexRec(n);

    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(end - start);

    cout << "Operations = " << operations << endl;
    cout << "Recursion Depth = " << maxDepth << endl;
    cout << "Time Taken (microseconds) = " << duration.count() << endl;

    return 0;
}

/*
Recurrence Relation:
T(n) = 3T(n/2) + n log n

Time Complexity:
O(n^(log2 3)) ≈ O(n^1.585)

Recursion Depth:
O(log n)
*/
