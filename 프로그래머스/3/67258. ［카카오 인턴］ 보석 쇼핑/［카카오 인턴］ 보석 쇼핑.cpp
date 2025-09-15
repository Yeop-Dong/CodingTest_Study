#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
using namespace std;

vector<int> solution(vector<string> gems) {
    vector<int> answer(2);
    map<string, int> m;
    set<string> s(gems.begin(), gems.end());
    int start = 0, end = 0, minimum;
    
    for(auto g : gems){
        m[g]++;
        if (m.size() == s.size()) break;
        end++;
    }
    
    minimum = end - start;
    answer[0] = start + 1;
    answer[1] = end + 1;
    
    while(end < gems.size()){
        string gem = gems[start];
        m[gem]--;
        start++;
        
        if (m[gem] == 0){
            end++;
            for(; end < gems.size(); end++){
                m[gems[end]]++;
                if (gem == gems[end])
                    break;
            }
            if (end == gems.size()) break;
        }
        if (minimum > end - start){
            answer[0] = start + 1;
            answer[1] = end + 1;
            minimum = end - start;
        }
    }
    
    return answer;
}