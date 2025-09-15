#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<string> good = {"()", "[]", "{}"};

bool good_parenthesis(string exp){
    int s, i;
    
    while((s = exp.size())){
        for(int i = 0; i < exp.size() - 1; i++){
            for(auto g : good){
                if (g == exp.substr(i, 2)){
                    exp.erase(i, 2);
                    break;
                }
            }
            if (s != exp.size())
                break;
        }
        if (s == exp.size())
            return false;
    }
    
    return true;
}

string rotate_left(string exp, int cnt){
    return exp.substr(cnt) + exp.substr(0, cnt);
}
int solution(string s) {
    int answer = 0;
    
    for(int i = 0; i < s.size(); i++){
        if (good_parenthesis(rotate_left(s, i)))
            answer++;
    }
    
    return answer;
}