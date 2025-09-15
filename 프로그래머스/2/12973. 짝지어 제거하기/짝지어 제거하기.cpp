#include <iostream>
#include<string>
using namespace std;

int solution(string s)
{
    int answer = -1;

    string st;
    
    for(auto i : s){
        if (st.empty()){
            st.push_back(i);
        }
        else if (st.back() == i){
            st.pop_back();
        }
        else{
            st.push_back(i);
        }
    }
    
    return st.empty();
    
    
}