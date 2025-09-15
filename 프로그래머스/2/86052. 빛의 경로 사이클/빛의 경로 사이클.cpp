#include <string>
#include <vector>
#include <map>
#include <algorithm>

#include <iostream>

using namespace std;

constexpr int UP = 0, DOWN = 1, LEFT = 2, RIGHT = 3;
map<int, pair<int, int>> MOVE = { {UP, {-1, 0}},
                                 {DOWN, {1, 0}},
                                 {LEFT, {0, -1}},
                                 {RIGHT, {0, 1}} };
struct node{
    char prop;
    vector<bool> visit = vector<bool>(4, false);
    
    node(){}
    node(char prop){this->prop = prop;}
};

int next_dir(node n, int dir){
    if (n.prop == 'L')
        switch(dir){
            case UP: return LEFT;
            case DOWN: return RIGHT;
            case LEFT: return DOWN;
            case RIGHT: return UP;
        }
    if (n.prop == 'R')
        switch(dir){
            case UP: return RIGHT;
            case DOWN: return LEFT;
            case LEFT: return UP;
            case RIGHT: return DOWN;
        }
    
    return dir;
}

int light(vector<vector<node>> &g, pair<int, int> pos, int dir){
    int cnt = 0;
    while(!g[pos.first][pos.second].visit[dir]){
        
        g[pos.first][pos.second].visit[dir] = true;
        pos.first = pos.first + MOVE[dir].first;
        pos.second = pos.second + MOVE[dir].second;
        if(pos.first < 0) pos.first = g.size()-1;
        else if (pos.first >= g.size()) pos.first = 0;
        if (pos.second < 0) pos.second = g[0].size() -1;
        else if (pos.second >= g[0].size()) pos.second = 0;
        
        dir = next_dir(g[pos.first][pos.second], dir);
        cnt++;
    }
    return cnt;
}

vector<int> solution(vector<string> grid) {
    vector<int> answer;
    vector<vector<node>> g;
    
    for(auto i : grid){
        g.push_back(vector<node>());
        for (auto j : i)
            g.back().push_back(j);
    }
    
    for(int i = 0; i < g.size(); i++)
        for(int j = 0; j < g[i].size(); j++)
            for(int dir = 0; dir < 4; dir++){
                int size = light(g, {i, j}, dir);
                if (size) answer.push_back(size);
            }
            
    sort(answer.begin(), answer.end());        
    
    
    return answer;
}