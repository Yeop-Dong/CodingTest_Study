#include <string>
#include <vector>
#include <tuple>

using namespace std;

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    int answer = 0;
    const int max_fare = n * (n - 1) / 2 * 100000 + 1;
    vector<vector<int>> g(n+1, vector<int>(n+1, max_fare));
    
    for(auto i = 1; i <= n; i++)
        g[i][i] = 0;
    
    for(auto f : fares){
        auto [from, to, weight] = tuple(f[0], f[1], f[2]);
        
        g[from][to] = weight;
        g[to][from] = weight;
    }
    
    for(int k = 1; k <= n; k++)
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= n; j++){
                if (g[i][k] == max_fare || g[k][j] == max_fare)
                    continue;
                g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
            }
    
    answer = max_fare;
    answer = min(answer, g[s][a] + g[s][b]);
    
    for(int k = 1; k <= n; k++){
        int k_fare = g[s][k] + g[k][a] + g[k][b];
        answer = min(answer, k_fare);
    }
    
    
    return answer;
}