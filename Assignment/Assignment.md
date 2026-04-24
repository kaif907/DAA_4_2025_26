# DAA Assignment

## 1. N-Queens Problem

### Problem Statement
Place N queens on an N × N chessboard such that no two queens attack each other.

A queen can attack:
- Same row  
- Same column  
- Same diagonal  

The task is to place all queens safely.

---

## Tasks
- Print all possible solutions  
- Count total number of valid configurations  
- Optimize using column and diagonal hashing  

---

## Algorithm

1. Start placing queens row by row.
2. For each row, try every column.
3. Check if position is safe using:
   - Column hash array  
   - Left diagonal hash array  
   - Right diagonal hash array  
4. If safe:
   - Place queen  
   - Mark hashes  
   - Recur for next row  
5. Backtrack after recursion.
6. Store all valid solutions.
7. Count total solutions.

---

## C++ Code

```cpp
#include<iostream>
#include<vector>
using namespace std;

class NQueens {
public:

vector<vector<string>> solutions;
int countSolutions=0;

void solve(int row,int n,
vector<string>& board,
vector<int>& col,
vector<int>& diag1,
vector<int>& diag2){

if(row==n){
solutions.push_back(board);
countSolutions++;
return;
}

for(int c=0;c<n;c++){

if(col[c]==0 &&
diag1[row-c+n-1]==0 &&
diag2[row+c]==0){

board[row][c]='Q';

col[c]=1;
diag1[row-c+n-1]=1;
diag2[row+c]=1;

solve(row+1,n,board,col,diag1,diag2);

board[row][c]='.';

col[c]=0;
diag1[row-c+n-1]=0;
diag2[row+c]=0;
}
}
}

void run(int n){

vector<string> board(n,string(n,'.'));

vector<int> col(n,0);
vector<int> diag1(2*n-1,0);
vector<int> diag2(2*n-1,0);

solve(0,n,board,col,diag1,diag2);

cout<<"Total Solutions: "<<countSolutions<<endl;

for(auto sol:solutions){

for(auto row:sol)
cout<<row<<endl;

cout<<endl;
}
}
};

int main(){

NQueens obj;
obj.run(4);

return 0;
}
```

---

## Time Complexity

```text
O(N!)
```

---

## Space Complexity

```text
O(N)
```

---

## Dry Run (N=4)

One solution:

```text
. Q . .
. . . Q
Q . . .
. . Q .
```

Second solution:

```text
. . Q .
Q . . .
. . . Q
. Q . .
```

Total Solutions:

```text
2
```

---

# 2. Hamiltonian Cycle

## Problem Statement

Given an undirected graph, determine whether a Hamiltonian cycle exists.

Hamiltonian Cycle:
A cycle that visits every vertex exactly once and returns to the starting vertex.

Use adjacency matrix representation.

---

## Tasks

- Print one valid cycle if it exists  
- Return false otherwise  
- Use adjacency matrix representation  

---

## Algorithm

1. Start from vertex 0.
2. Add vertices one by one.
3. Check whether:
   - Vertex is adjacent  
   - Vertex not already used  
4. If valid, include it.
5. Recur for next position.
6. If all vertices used:
   - Check edge back to first node.
7. If yes:
   - Hamiltonian cycle exists.
8. Else backtrack.

---

## C++ Code

```cpp
#include<iostream>
using namespace std;

#define V 5

bool isSafe(int v,int graph[V][V],int path[],int pos){

if(graph[path[pos-1]][v]==0)
return false;

for(int i=0;i<pos;i++)
if(path[i]==v)
return false;

return true;
}

bool hamCycleUtil(int graph[V][V],int path[],int pos){

if(pos==V){

if(graph[path[pos-1]][path[0]]==1)
return true;
else
return false;
}

for(int v=1;v<V;v++){

if(isSafe(v,graph,path,pos)){

path[pos]=v;

if(hamCycleUtil(graph,path,pos+1)==true)
return true;

path[pos]=-1;
}
}

return false;
}

bool hamCycle(int graph[V][V]){

int path[V];

for(int i=0;i<V;i++)
path[i]=-1;

path[0]=0;

if(hamCycleUtil(graph,path,1)==false){

cout<<"No Hamiltonian Cycle"<<endl;

return false;
}

cout<<"Hamiltonian Cycle:"<<endl;

for(int i=0;i<V;i++)
cout<<path[i]<<" ";

cout<<path[0]<<endl;

return true;
}

int main(){

int graph[V][V]={
{0,1,1,0,1},
{1,0,1,1,1},
{1,1,0,1,0},
{0,1,1,0,1},
{1,1,0,1,0}
};

hamCycle(graph);

return 0;
}
```

---

## Time Complexity

```text
O(V!)
```

---

## Space Complexity

```text
O(V)
```

---

## Dry Run

Path construction:

```text
0 → 1 → 2 → 3 → 4
```

Check last edge:

```text
4 → 0 exists
```

Hamiltonian Cycle:

```text
0 1 2 3 4 0
```

---

## Repository Structure

```text
DAA/
└── Assignment/
    ├── nqueens.cpp
    ├── hamiltonian.cpp
    ├── algorithm.md
    ├── complexity.md
    └── dry_run.md
```
