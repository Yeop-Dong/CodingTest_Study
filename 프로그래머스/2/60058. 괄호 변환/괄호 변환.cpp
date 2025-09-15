#include <string>
#include <vector>
#include <tuple>
#include <iostream>

using namespace std;

bool isgood(string p){
    vector<char> st;
    
    for(auto c : p){
        if (c == '('){
            st.push_back(c);
        }
        if (c == ')'){
            if (st.empty())
                return false;
            else
                st.pop_back();
        }
    }
    
    return true;
}

pair<string, string> divideParenthesis(string p){
    int cnt_open = 0, cnt_close = 0, i;
    
    for(i = 0; i < p.size(); i++){
        if (p[i] == '(') cnt_open++;
        else if (p[i] == ')') cnt_close++;
        
        if (cnt_open && cnt_close && cnt_open == cnt_close)
            break;
    }
    
    return {p.substr(0, i+1), p.substr(i+1)};
}

string oppose(string p){
    for(auto &c : p){
        if (c == '(') c = ')';
        else c = '(';
    }
    return p;
}
string correction(string p){
    if (p.empty()) return "";
    string u, v;
    
    tie(u, v) = divideParenthesis(p);
    if (isgood(u)){
        return u + correction(v);
    }
    else{
        u = u.substr(1, u.size()-2);
        return "(" + correction(v) + ")" + oppose(u);
    }
}

string solution(string p) {
    
    if (isgood(p)) 
        return p;
    else 
        return correction(p);
}