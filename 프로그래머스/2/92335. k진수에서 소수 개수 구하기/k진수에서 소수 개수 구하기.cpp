#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
using namespace std;


bool is_prime(long long n){
    if (n == 1) return false;
    
    for(long long i = 2; i * i <= n; i++)
        if (n % i == 0)
            return false;
    return true;
}
int solution(int n, int k) {
    int answer = 0;
    string num = "";
    while(n){
        num = to_string(n % k) + num;
        n /= k;
    }
    
   
    
    stringstream ss(num);
    string tmp;
    
    vector<long long> cand;
    while(getline(ss, tmp, '0')){
        if (tmp.size() == 0) continue;
        long long p = stol(tmp);
        cand.push_back(p);
    }
    
    
    for(auto c : cand)
        if (is_prime(c)) answer++;

    return answer;
}