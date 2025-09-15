#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int pc= 0, yc = 0;
    for(auto c : s){
        if (c == 'p' || c=='P') pc++;
        if (c == 'y' || c =='Y') yc++;
    }
    
    answer = pc == yc;
    return answer;
}