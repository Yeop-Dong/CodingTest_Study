#include <string>
#include <vector>

using namespace std;

int gcd(int a, int b){
    return b ? gcd(b, a%b) : a;
}

vector<int> solution(int n, int m) {
    int g = gcd(n, m);
    int l = n * m / g;
    vector<int> answer = {g, l};
    
    return answer;
}