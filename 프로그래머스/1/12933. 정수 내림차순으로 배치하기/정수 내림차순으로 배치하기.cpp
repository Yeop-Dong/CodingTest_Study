#include <string>
#include <vector>
#include <algorithm>
using namespace std;

long long solution(long long n) {
    long long answer = 0;
    
    string ns = to_string(n);
    sort(ns.begin(), ns.end(), greater<int>());
    answer = stoll(ns);
    
    return answer;
}