#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

int NNN(int N, int times){
    int res = N;
    while(--times)
        res = res * 10 + N;
    return res;
}

int solution(int N, int number) {
    int answer = 0;
    vector<set<int>> dp(9);
    
    for(int i = 1; i < 9; i++){
        
        dp[i].insert(NNN(N, i));
        for(int j = 1; j < i; j++){
            for(auto di : dp[j]){
                for(auto dj : dp[i-j]){
                    dp[i].insert(di + dj);
                    dp[i].insert(di - dj);
                    dp[i].insert(di * dj);
                    if (dj) dp[i].insert(di / dj);
                }
            }
        }
        
        if (dp[i].find(number) != dp[i].end())
            return i;
    }
    
    for(auto d : dp[4]){
        cout << d << " ";
    }
    return -1;
}