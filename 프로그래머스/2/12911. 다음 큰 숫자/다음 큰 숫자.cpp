#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(int n) {
    int answer = n;
    
    int i = 0, cnt = 0;
    bool flag = false;
    while(n){
        if (n & 1){
            flag = true;
            cnt++;
        }
        
        n >>= 1;
        i++;
        
        if (!(n & 1) && flag)
            break;
    }
    
    answer = answer | (1 << i);
    cnt--;
    for(int ones = 0; ones < cnt; ones++)
        answer = answer | (1 << ones);
    
    for(int zeros = cnt; zeros < i; zeros++){
        if (answer & (1 << zeros))
            answer = answer - (1 << zeros);
    }
        
    
    return answer;
}