#include <string>
#include <vector>
using namespace std;

bool ETT[1000001] = {true,};

int solution(int n) {
    int answer = 0;

    for(int i = 2; i <= n; i++){
        if (ETT[i]) continue;
        answer++;
        for(int j = i; j <= n; j += i) ETT[j] = true;
    }
    
    return answer;
}