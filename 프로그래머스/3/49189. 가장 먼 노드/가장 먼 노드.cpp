#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    vector<vector<int>> g(n+1);
    
    for(auto e : edge){
        g[e[0]].push_back(e[1]);
        g[e[1]].push_back(e[0]);
    }
    
    vector<int> dist(n+1, -1);
    queue<int> q;
    
    q.push(1);
    dist[1] = 0;
    
    while(!q.empty()){
        int u = q.front();
        q.pop();
        for(int v : g[u]){
            if (dist[v] == -1){
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    
    int max_dist = *max_element(dist.begin() + 1, dist.end());
    
    for(int i = 1; i < n+1; i++){
        if (dist[i] == max_dist) answer++;
    }
    
    return answer;
}