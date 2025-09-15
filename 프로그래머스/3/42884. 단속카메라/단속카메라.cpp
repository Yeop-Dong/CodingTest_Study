#include <string>
#include <vector>
#include <algorithm>
#include <map>

#include <iostream>

using namespace std;

int solution(vector<vector<int>> routes) {
    int answer = 0;
    
    sort(routes.begin(), routes.end(), [](auto l, auto r){
        return l[1] < r[1];
    });
    
    vector<int> cam;
    
    for(auto r : routes){
        
        if (cam.empty()){
            cam.push_back(r[1]);
            continue;
        }
        int last = cam.back();
        if (r[0] > last)
            cam.push_back(r[1]);

    }
    
    return cam.size();
    
}