#include <string>
#include <vector>

using namespace std;


int solution(int n) {
    
    int ans = 0;
    for(int start = 1; start <= n; start++){
        int sum = 0;
        for(int i = start; sum < n; i++){
            sum += i;
        }
        if (sum == n) ans++;
    }
    
    return ans;
}