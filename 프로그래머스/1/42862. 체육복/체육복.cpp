#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> st(n, 1);
    for(auto r : reserve){
        st[r-1]++;
    }
    for(auto l : lost){
        st[l-1]--;
    }
    
    for(int i = 0; i < st.size(); i++){
        if (st[i] > 1){
            if (i)
                if (!st[i-1]){
                    st[i]--;
                    st[i-1]++;
                    continue;
                }
            
            if (!st[i+1]){
                st[i]--;
                st[i+1]++;
                continue;
            }
                    
        }
    }
    
    for(auto s : st){
        if (s) answer++;
    }
    
    
    return answer;
}