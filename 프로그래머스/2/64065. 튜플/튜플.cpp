#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    
    s = s.substr(1, s.size() - 2);
    
    vector<vector<int>> sets;
    sets.push_back(vector<int>());
    
    int start = 0;
    bool open = false;
    for(int i = 0; i < s.size(); i++){
        switch(s[i]){
            case ',':
                if (open) {
                    sets.back().push_back(stoi(s.substr(start, i - start)));
                    start = i + 1;
                }
                break;
            case '{':
                open = true;
                start = i + 1;
                break;
            case '}':
                open = false;
                sets.back().push_back(stoi(s.substr(start, i - start)));
                sets.push_back(vector<int>());
                break;
        }
    }
    sort(sets.begin(), sets.end(), [](vector<int> a, vector<int> b){
       return a.size() < b.size(); 
    });
    
    for(int i = 1; i < sets.size(); i++){
        for(auto e : sets[i]){
            auto it = find(answer.begin(), answer.end(), e);
            if (it == answer.end())
                answer.push_back(e);
        }
    }
    
    return answer;
}