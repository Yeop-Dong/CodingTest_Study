#include <string>
#include <vector>
#include <map>
#include <functional>
#include <iostream>

using namespace std;

int solution(string begin, string target, vector<string> words) {
    int answer = 51;

    int start = words.size(), end;
    words.push_back(begin);
    vector<vector<int>> g(words.size(), vector<int>());
    
    for(int i = 0; i < words.size(); i++){
        if (target == words[i])
            end = i;
        for(int j = i + 1; j < words.size(); j++){
            if (i == j) 
                continue;
            
            int cnt = 0;
            for(int k = 0; k < words[i].size(); k++){
                if (words[i][k] != words[j][k])
                    cnt++;
                if(cnt > 1)
                    break;
            }
            if (cnt == 1){
                g[i].push_back(j);
                g[j].push_back(i);
            }
        }
    }
    
    vector<int> d(words.size(), 0);
    
    function<void(int, int)> dfs = [&](int i, int step)->void{
        
        if (answer <= step)
            return;
        
        if (i == end){
            answer = min(answer, step);
            return;
        }
        
        for(auto k : g[i]){
            if (d[k] == 0){
                d[k] = 1;
                dfs(k, step+1);
                d[k] = 0;
            }
        }
    };
    
    dfs(start, 0);
    if (answer == 51)
        return 0;
    return answer;

}