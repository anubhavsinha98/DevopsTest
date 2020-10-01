#include <iostream>
using namespace std;

int dp[100][100];


int main() {
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    int x;
    cin>>x;
    for(int i=0;i<=n;i++){
        dp[i][0] = 1;
    }
    for(int j=1;j<=x;j++){
        dp[0][j] = 0;
    }
    for(int i=1;i<=n;i++){
        for(int j=1;j<=x;j++){
            if (arr[i-1] <= j){
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]];
            }
            else{
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    cout<<dp[n][x];
    
}