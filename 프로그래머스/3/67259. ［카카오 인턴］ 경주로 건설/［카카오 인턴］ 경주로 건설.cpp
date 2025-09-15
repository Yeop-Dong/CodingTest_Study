#include <string>
#include <vector>
#include <queue>
#include <tuple>
#include <map>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> board) {

    auto n = board.size();
    const int up = 0, down = 1, left = 2, right = 3;
    
    map<int, pair<int, int>> delta = { {up, {-1, 0}}, {down, {1, 0}},
                                        {left, {0, -1}}, {right, {0, 1}} };
    vector<vector<vector<int>>> dist(n, vector<vector<int>>(n, vector<int>(4, 25*25*600)));
    queue<tuple<int, int, int, int>> q;
    
    for(auto [dir, _] : delta){
        dist[0][0][dir] = 0;
    }
    q.push({0, 0, -1, 0});
    
    while(!q.empty()){
        auto [y, x, d_prev, cost_prev] = q.front();
        q.pop();
        for(auto [dir, move] : delta){
            auto [dy, dx] = move;
            auto [ny, nx] = pair(y + dy, x + dx);
            
            if (ny < 0 || ny >= n || nx < 0 || nx >= n)
                continue;
            if (board[ny][nx])
                continue;
            
            bool turn = d_prev != -1 && (d_prev <= down ? dir >= left : dir <= down);
            int cost = cost_prev + (turn ? 600 : 100);
            
            if (cost < dist[ny][nx][dir]){
                q.push({ny, nx, dir, cost});
                dist[ny][nx][dir] = cost;
            }
        }
    }
    
    return *min_element(dist[n-1][n-1].begin(), dist[n-1][n-1].end());
}