#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool compare(vector<int> a, vector<int> b){
    if (a[1] == b[1])
            return a[0] < b[0];
    return a[1] < b[1];
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    
    sort(dungeons.begin(), dungeons.end(), compare);
    
    do{
        int t = k, cnt = 0;
        for(auto d : dungeons){
            if (t < d[0]) continue;
            
            t -= d[1];
            cnt++;
        }
        
        if (answer < cnt)
            answer = cnt;
    }while(next_permutation(dungeons.begin(), dungeons.end()));

    
    return answer;
}