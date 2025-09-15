#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int w, int h) {
    long long answer = 0;
    long long top;
    
    for(int i = 1; i < w; i++){
        top = h * i;
        answer += top / w;
    }
    return answer * 2;
}