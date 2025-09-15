#include <string>
#include <vector>
#include <iostream>

using namespace std;

string tobin(int i){
    string bin = "";
    
    while(i > 0){
        bin = to_string(i & 1) + bin;
        i >>= 1;
    }
    
    return bin;
}
vector<int> solution(string s) {
    vector<int> answer;
    vector<int> cnt;
    int icnt = 0, zcnt;
    do{
        int len = 0;
        for(auto c : s){
            if (c == '0')
                len++;
        }
        cnt.push_back(len);
        len = s.size() - len;
        s = tobin(len);
    }while(s != "1");
    
    int iter = 0, sum = 0;
    for(auto c : cnt){
        sum += c;
        iter++;   
    }
    
    answer.push_back(iter);
    answer.push_back(sum);
    return answer;
}