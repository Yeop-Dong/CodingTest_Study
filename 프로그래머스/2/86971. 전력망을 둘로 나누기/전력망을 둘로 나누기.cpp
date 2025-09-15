#include <string>
#include <vector>
#include <iostream>


using namespace std;


int dfs(int start, vector<vector<int>> &g, vector<bool> v, pair<int, int> ex){
    
    v[start] = true;
    int sum = 1;
    
    for(auto n : g[start]){
        if (v[n]) continue;
        if (start == ex.first && n == ex.second || \
           start == ex.second && n == ex.first) continue;
        sum += dfs(n, g, v, ex);
    }
    
    return sum;
}
int solution(int n, vector<vector<int>> wires) {
    int answer = n;
    
    vector<vector<int>> g(n+1, vector<int>());
    
    for(auto w : wires){
        int v1 = w[0], v2 = w[1];
        
        g[v1].push_back(v2);
        g[v2].push_back(v1);
    }
    
    for(auto w : wires){
        int v1 = w[0], v2 = w[1];
        vector<bool> visited1(n+1, false);
        int s1 = dfs(v1, g, visited1, {v1, v2});
        vector<bool> visited2(n+1, false);
        int s2 = dfs(v2, g, visited2, {v1, v2});
        int dif = s1 - s2 > 0 ? s1 - s2 : s2 - s1;
        
        if (answer > dif) answer = dif;
    }
    
    
    return answer;
}