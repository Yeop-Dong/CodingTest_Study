#include <string>
#include <vector>
#include <iostream>

using namespace std;


vector<int> solution(int n) {
    vector<int> answer;
    vector<vector<int>> tri;
    int size, num, dir;
    vector<pair<int, int>> move = { {1, 0}, {0, 1}, {-1, -1} };
    
    for(int i = 1; i <= n; i++) 
        tri.push_back(vector<int>(i, 0));
    
    num = 1;
    size = n * (n + 1) / 2;
    dir = 0;
    pair<int, int> pos = {0, 0};
    tri[pos.first][pos.second] = num++;
    
    
    while(num <= size){
        pair<int, int> new_pos;
        
        new_pos.first = pos.first + move[dir].first;
        new_pos.second = pos.second + move[dir].second;
        if (new_pos.first < new_pos.second || new_pos.first < 0 || \
            new_pos.first >= n || tri[new_pos.first][new_pos.second]){
            dir = (dir + 1) % 3;
            continue;
        }
        
        pos = new_pos;
        tri[pos.first][pos.second] = num++;
    }
    
    for(auto t : tri){
        for(auto i : t)
            answer.push_back(i);
    }
    
    return answer;
}