#include <string>
#include <vector>

using namespace std;
constexpr long long DIV = 1000000007;
long long dp[2501];
int solution(int n) {
    int answer = 0;
    
    if (n & 1) return 0;
    
    n = n / 2;
    
    dp[0] = 1;
    dp[1] = 3;
    dp[2] = 11;
    for(int i = 3; i <= n; i++){
        dp[i] = dp[i - 1] * 3 % 1000000007;
        for(int j = 0; j < i - 1; j++){
            dp[i] += dp[j] * 2;
            dp[i] %= 1000000007;
        }
        dp[i] = dp[i] % 1000000007;
    }
    
    return dp[n] % 1000000007;
}