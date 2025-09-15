#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    
    int deci = 1;
    for(int i = s.size()-1; i >= 0; i--){
        switch(s[i]){
            case '+': break;
            case '-':
                answer *= -1;
                break;
            default:
                answer += deci * (s[i] - '0');
                deci *= 10;
                break;
        }
    }
    
    return answer;
}