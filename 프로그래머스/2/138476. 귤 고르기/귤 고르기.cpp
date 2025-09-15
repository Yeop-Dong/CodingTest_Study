#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <iostream>


using namespace std;

int solution(int k, vector<int> tangerine) {
    int answer = 0;
    map<int, int> cnts;
    
    int total = 0;
    for(auto t : tangerine)
        cnts[t]++;
    
    vector<int> v;
    for(auto [_, c]: cnts)
        v.push_back(c);
    sort(v.rbegin(), v.rend());
    
    for(auto i : v){
        total += i;
        answer++;
        if (total >= k) break;
    }
    
    
    return answer;
}