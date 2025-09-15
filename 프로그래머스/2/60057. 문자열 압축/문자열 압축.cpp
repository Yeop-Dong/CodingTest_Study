#include <string>
#include <vector>
#include <iostream>


using namespace std;

string compress(string s, int unit){
    
    if (s.length() < unit) return s;
    
    string prefix = s.substr(0, unit);
    int cnt = 1;
    while(s.substr(cnt * unit, unit) == prefix)
        cnt++;
    
    string answer = "";
    if (cnt > 1) answer += to_string(cnt);
    return answer + prefix + compress(s.substr(cnt*unit), unit);
}

int solution(string s) {
    int answer = 0;
    
    int min = 0;
    for(int i = 1; i <= s.length(); i++){
        int len = compress(s, i).length();
        //cout << i << ":\t" << len << "\t" << compress(s, i) << endl;
        if (min == 0) min = len;
        if (min > len) min = len;
    }
    
    answer = min;
    return answer;
}