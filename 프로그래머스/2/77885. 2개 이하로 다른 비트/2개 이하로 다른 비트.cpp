#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<long long> solution(vector<long long> numbers) {
    vector<long long> answer;
    
    for(auto n : numbers){
        int k = 0;
        
        while(n >> k){
            if ((n >> k & 1) == 0) break;
            k++;
        }
        
        
        if (k)
            n += 1LL << (k - 1);
        else
            n += 1;
        
        answer.push_back(n);
        
    }
    
    return answer;
}