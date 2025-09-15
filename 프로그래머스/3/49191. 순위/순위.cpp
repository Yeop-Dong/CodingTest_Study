#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    
    vector<vector<bool>> dist(n+1, vector<bool>(n+1, false));
    
    for(auto r : results)
        dist[r[0]][r[1]] = true;
    
    for(int k = 1; k <= n; k++)
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= n; j++)
                if (dist[i][k] && dist[k][j])
                    dist[i][j] = true;
    
    for(int i = 1; i <= n; i++){
        int count = 0;
        for(int j = 1; j<= n; j++){
            if (dist[i][j] || dist[j][i])
                count++;
        }
        if (count == n - 1)
            answer++;
    }
        
    
    return answer;
}