#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int rotate(vector<vector<int>> & arr, vector<int> query){
    pair<int, int> top = {query[0] - 1, query[1] - 1}, bot = {query[2] - 1, query[3] -1};
    const int right = 0, down = 1, left = 2, up = 3;
    vector<pair<int, int>> move = { {0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    vector<pair<int, int>> border = { {top.first, bot.second}, bot, {bot.first, top.second}, top};
    
    pair<int, int> coor = top;
    int direction = right;
    
    vector<int> data;
    do {
        data.push_back(arr[coor.first][coor.second]);
        
        coor.first += move[direction].first;
        coor.second += move[direction].second;
        
        if (coor == border[direction]){
            direction = (direction + 1) % 4;
        }
        
    }while(coor != top);
    
    for(auto d : data){
        
        coor.first += move[direction].first;
        coor.second += move[direction].second;
        
        if (coor == border[direction]){
            direction = (direction + 1) % 4;
        }
        
        arr[coor.first][coor.second] = d;
    }
    
    return *min_element(data.begin(), data.end());
    
}
vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
    vector<vector<int>> arr(rows, vector<int>(columns, 0));
    
    int k = 0;
    for(auto &i : arr){
        for(auto &j : i){
            j = ++k;
        }
    }
    
    for(auto q : queries){
        answer.push_back(rotate(arr, q));

    }
    
    return answer;
}