#include <vector>
using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, int m, vector<vector<int>> edge_list, int k, vector<int> gps_log) {
    vector<vector<bool>> g(n+1, vector<bool>(n+1, false));
    
    for(auto e : edge_list)
        g[e[0]][e[1]] = g[e[1]][e[0]] = true;
    
    vector<vector<int>> dp(k, vector<int>(n+1, 200));
    dp[0][gps_log.front()] = 0;
    
    for(int i = 1; i < k; i++){
        for(int j = 1; j <= n; j++){
            dp[i][j] = min(dp[i][j], dp[i-1][j]);
            for(int c = 1; c <= n; c++)
                if (g[j][c])
                    dp[i][j] = min(dp[i][j], dp[i-1][c]);
            if (j != gps_log[i]) dp[i][j]++;
        }
    }
    
    
    if (dp.back()[gps_log[k-1]] < 200) 
        return dp.back()[gps_log[k-1]];
    else 
        return -1;
    
    
}