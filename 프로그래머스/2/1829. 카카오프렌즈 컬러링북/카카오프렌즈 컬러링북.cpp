#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int expand(vector<vector<int>> picture, vector<vector<int>> &area, pair<int, int> pos, int num){
    
    
    int y = pos.first, x = pos.second;
    int color = picture[y][x];
    
    if (area[y][x] != 0) return 0;
    if (color == 0) return 0;
    
    int u, d, l, r;
    
    u = d = l = r = 0;
    
    area[y][x] = num;
    
    
    if (y > 0 && picture[y-1][x] == color) 
        u = expand(picture, area, {y-1, x}, num);
    
    if (y+1 < picture.size() && picture[y+1][x] == color) 
        d = expand(picture, area, {y+1, x}, num);
    
    if (x > 0 && picture[y][x-1] == color) 
        l = expand(picture, area, {y, x-1}, num);
    
    if (x+1 < picture[0].size() && picture[y][x+1] == color) 
        r = expand(picture, area, {y, x+1}, num);
    
    return u + d + l + r + 1;
}

pair<int, int> find_next_area(vector<vector<int>> picture, vector<vector<int>> area){
    for(int i = 0; i < area.size(); i++){
        for(int j = 0; j < area[i].size(); j++){
            if (area[i][j] == 0 && picture[i][j] != 0)
                return {i, j};
        }
    }
    return {-1, -1};
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    
    vector<vector<int>> area(m, vector<int>(n, 0));
    vector<int> area_info;
    pair<int, int> pos = find_next_area(picture, area);
    int areanum = 1;
    
    
    while(pos.first != -1){
       
        int size = expand(picture, area, pos, areanum++);
         pos = find_next_area(picture, area);
        
        area_info.push_back(size);
    }
    
    for(auto a : area){
        for (auto i : a){
            cout << i << "\t";
        }
        cout << endl;
    }
    
    for(auto a : area_info){
        cout << a << " ";
    }
    vector<int> answer(2);
    answer[0] = number_of_area = area_info.size();
    answer[1] = max_size_of_one_area = *max_element(area_info.begin(), area_info.end());
    return answer;
}