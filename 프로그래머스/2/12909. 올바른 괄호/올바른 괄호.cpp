#include<string>
#include <iostream>
#include <vector>

using namespace std;

bool solution(string s)
{
    vector<char> st;
    for(auto c : s){
        if (c == '(')
            st.push_back(c);
        else{
            if (st.empty())
                return false;
            if (st.back() != '(')
                return false;
            
            st.pop_back();
        }
    }
    

    return st.empty();
}