#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long solution(int k, int d) {
    long long answer = 0;
    long long dd = (long long)d * d;
    for(long long x = 0; x <= d; x +=k){
        long long y = (long long)sqrt(dd - x*x);
        answer += y / k + 1;
    }
    return answer;
}