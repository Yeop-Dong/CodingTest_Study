#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<string> solution(vector<vector<int>> line) {
    
    vector<pair<long long, long long>> point;
    
    for(int i = 0; i < line.size(); i++){
        for (int j = i + 1; j < line.size(); j++){
            long long A = line[i][0];
            long long B = line[i][1];
            long long C = line[j][0];
            long long D = line[j][1];
            long long E = line[i][2];
            long long F = line[j][2];
            
            if (A * D == B * C) continue;
            
            double y = -1 * static_cast<double>(E * C - A * F) / (A * D - B * C);
            double x = static_cast<double>(B * F - E * D) / (A * D - B * C);
            
            if (y == static_cast<long long>(y) && x == static_cast<long long>(x))
                point.push_back({static_cast<long long>(y), static_cast<long long>(x)});
        }
    }
    long long min_y = min_element(point.begin(), point.end(), \
                             [](auto a, auto b)->bool {
                                return a.first < b.first; 
                             })->first;
    long long min_x = min_element(point.begin(), point.end(), \
                            [](auto a, auto b)->bool {
                               return a.second < b.second; 
                            })->second;
    
    
    for(auto &p : point){
        p.first -= min_y;
        p.second -= min_x;
    }
                
    long long max_y = max_element(point.begin(), point.end(), \
                                  [](auto a, auto b)->bool {
                                      return a.first < b.first; 
                                  })->first;
    long long max_x = max_element(point.begin(), point.end(), \
                                  [](auto a, auto b)->bool {
                                      return a.second < b.second; 
                                  })->second;
    
    
    vector<string> answer(max_y + 1, string(max_x + 1, '.'));
    
    for(auto p : point){
        answer[p.first][p.second] = '*';
    }
    
    return answer;
}