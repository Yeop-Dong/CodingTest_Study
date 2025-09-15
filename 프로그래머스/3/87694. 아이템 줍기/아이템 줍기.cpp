#include <string>
#include <vector>
#include <tuple>

using namespace std;

bool is_inside(int x, int y, vector<vector<int>> &rectangle){
    for(auto r : rectangle){
        auto [x1, y1, x2, y2] = tuple(r[0], r[1], r[2], r[3]);
        if (x1 < x && x < x2 && y1 < y && y < y2)
            return true;
    }
    return false;
}

vector<pair<int, int>> dir = { {-1, 0}, {1 , 0}, {0, -1}, {0, 1}};
inline pair<int, int> pair_sum(pair<int, int> a, pair<int, int> b){
    return pair(a.first + b.first, a.second + b.second);
}
int dfs(vector<vector<bool>> &map, vector<vector<bool>> &visited, pair<int, int> pos, pair<int, int> end){
    
    if (pos == end)
        return 0;
    
    visited[pos.first][pos.second] = true;
    
    int m = 100000;
    for(auto d : dir){
        auto [ny, nx] = pair_sum(pos, d);
        if (ny < 1 || nx < 1 || ny > 100 || nx > 100)
            continue;
        if (map[ny][nx] == false)
            continue;
        if (visited[ny][nx] == true)
            continue;
        
        int tmp = 1 + dfs(map, visited, pair(ny, nx), end);
        if (m > tmp)
            m = tmp;
    }
    
    return m;
}

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    int answer = 0;
    vector<vector<bool>> map(101, vector<bool>(101, false));
    vector<vector<bool>> visited(101, vector<bool>(101, false));
    for(auto &r : rectangle)
        for(auto &c : r)
            c *= 2;
    
    for(auto r : rectangle){
        auto [x1, y1, x2, y2] = tuple(r[0], r[1], r[2], r[3]);
        for(int i = x1; i <= x2; i++){
            if (!is_inside(i, y1, rectangle))
                map[y1][i] = true;
            if (!is_inside(i, y2, rectangle))
                map[y2][i] = true;
        }
        for(int i = y1; i <= y2; i++){
            if (!is_inside(x1, i, rectangle))
                map[i][x1] = true;
            if (!is_inside(x2, i, rectangle))
                map[i][x2] = true;
        }
    }
    
    auto start = pair(characterY * 2, characterX * 2);
    auto end = pair(itemY * 2, itemX * 2);
    
    answer = dfs(map, visited, start, end) / 2;
    
    return answer;
}