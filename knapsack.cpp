#include<bits/stdc++.h>
using namespace std;

int dp[1001][1001];

int knapsack(int wt[], int val[], int w, int n){
    if (n==0 || w <= 0) {
        return 0;
    }
    if (dp[n][w] != -1){
        return dp[n][w];
    }
    if (wt[n-1] <= w) {
        dp[n][w] =  std::max(val[n-1] + knapsack(wt, val, w-wt[n-1], n-1), knapsack(wt, val, w, n-1));
        return dp[n][w];
    }
    else{
        dp[n][w] = knapsack(wt, val, w, n-1);
        return dp[n][w];
    }
}

int32_t main(){

    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    int t,n,w;
    cin>>t;
    while(t--){
        for(int i=0;i<1001;i++){
            for(int j=0;j<1001;j++){
                dp[i][j] = -1;
            }
        }
        cin>>n;
        cin>>w;
        int wt[n];
        int val[n];
        for(int i=0;i<n;i++){
            cin>>wt[i];
        }
        for(int i=0;i<n;i++){
            cin>>val[i];
        }
        cout<<knapsack(wt,val,w,n)<<endl;
    }
}