#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(int cacheSize, vector<string> cities) {
    int answer = 0;
    
    list<string> cache;
    
    for(auto c : cities){
        transform(c.begin(), c.end(), c.begin(), ::tolower);
        
        auto it = find(cache.begin(), cache.end(), c);
        if (it != cache.end()){
            // cash hit
            answer++;
            string tmp = *it;
            cache.erase(it);
            cache.push_front(tmp);
            continue;
        }
        
        //cash miss
        answer += 5;
        
        cache.push_front(c);
        if (cacheSize < cache.size()) cache.pop_back();
    }
    
    return answer;
}