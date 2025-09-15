#include <string>
#include <vector>

using namespace std;

long long memo[2001];

long long solution(int n) {
    long long answer = 0;
    
    memo[1] = 1;
    memo[2] = 2;
    
    for(int i = 3; i <= n; i++){
        memo[i] = (memo[i - 1] + memo[i - 2]) % 1234567;
    }
    return memo[n];
}