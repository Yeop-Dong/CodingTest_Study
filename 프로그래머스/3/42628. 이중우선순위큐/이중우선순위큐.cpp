#include <string>
#include <vector>
#include <set>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    set<int> pq;
    
    for(auto o : operations){
        if (o[0] == 'I'){
            int n = stoi(o.substr(2));
            pq.insert(n);
        }
        else if (o[2] == '1'){
            if (!pq.empty())
                pq.erase(prev(pq.end()));
        }
        else{
            if (!pq.empty())
                pq.erase(pq.begin());
        }
    }
    
    if (pq.empty())
        answer = vector<int>({0, 0});
    else
        answer = vector<int>({*prev(pq.end()), *pq.begin()});
    
    return answer;
}