#include <string>
#include <vector>

using namespace std;

int queen[12];

int nqueen(int cur, int n){
    if (cur == n)
        return 1;
    int res = 0;
    for(int i = 0; i < n; i++){
        queen[cur] = i;
        int j;
        for(j = 0; j < cur; j++){
            if (queen[j] == i || abs(queen[cur] - queen[j]) == cur - j)
                break;
        }
        if (j == cur)
            res += nqueen(cur + 1, n);
        
    }
    return res;
}

int solution(int n) {
    int answer = 0;
    
    return nqueen(0, n);
    
    
}