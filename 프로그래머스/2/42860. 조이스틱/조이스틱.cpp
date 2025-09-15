#include <string>
#include <vector>
#include <iostream>

using namespace std;

int from_A(char c){
    return (c - 'A') < ('Z' - c + 1) ? (c - 'A') : ('Z' - c + 1);
}

int solution(string name) {
    int answer = 0;
    int s = name.size();
    
    for(int i = 0; i < s; i++)
        answer += from_A(name[i]);
    
    /*
    case a)         case b)                       
    ~~~~AAAA~~~     ~~~~AAAA~~~
    ->1     3<-     ->3     1<-
    2<-                     ->2
    */
    
    int dist = s - 1, a_cnt = 0;
    
    for(int i = 0; i < s; i++){
        if (name[i] != 'A') continue;
        
        for(a_cnt = 1; i + a_cnt < s && name[i+a_cnt] == 'A'; a_cnt++);
        
        int a2, b2, min2;
        
        a2 = i - 1 < 0 ? 0 : i - 1;
        b2 = s - (i+a_cnt);
        
        min2 = min(a2, b2);
        dist = min(dist, a2 + b2 + min2);
    }
    answer += dist;
    
    return answer;
}