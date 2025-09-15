#include <iostream>
#include <vector>
#include <queue>

using namespace std;


int solution(int N, vector<vector<int> > road, int K) {
    int answer = 0;

    vector<pair<int, int>> g[N+1];
    
    for(auto r : road){
        int from = r[0], to = r[1], w = r[2];
        g[from].push_back({to, w});
        g[to].push_back({from, w});
    }
    
    int dist[N+1];
    fill(dist, dist+N+1, 10000000);
    priority_queue<pair<int, int>> q;
    
    q.push({0, 1});
    dist[1] = 0;
    
    while(!q.empty()){
        int d = -q.top().first;
        int u = q.top().second;
        q.pop();
        
        for(auto [v, w] : g[u]){
            if (dist[v] > w + dist[u]){
                dist[v] = w + dist[u];
                q.push({-dist[v], v});
            }
        }
        
    }
    
    for(int i = 1; i < N+1; i++){
        if (dist[i] <= K)
            answer++;
    }
    return answer;
}