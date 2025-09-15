#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

long long solution(int n, vector<int> times) {
    
    long long answer;
    long long l = 1, r = static_cast<long long>(n) * *max_element(times.begin(), times.end()), mid;
    
    while(l <= r){
        mid = (l + r) / 2;
        
        long long sum = 0;
        for(auto t : times){
            sum += mid / t;
        }
        
        if (sum >= n){
            answer = mid;
            r = mid - 1;
        }
        else{
            l = mid + 1;
        }
    }

    return answer;
}