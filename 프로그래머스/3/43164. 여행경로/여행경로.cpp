#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

vector<string> fly(map<string, multiset<string>> m, vector<string> answer, int size){
    
    if (answer.size() == size)
        return answer;
    
    auto cur = answer.back();
    if (m[cur].size() == 0)
        return answer;
    
    for(auto n : m[cur]){
        answer.push_back(n);
        auto sv = m;
        sv[cur].erase(sv[cur].find(n));    
        auto tmp = fly(sv, answer, size);
        if (tmp.size() == size)
            return tmp;
        answer.pop_back();
    }
    return vector<string>();
}
vector<string> solution(vector<vector<string>> tickets) {
    map<string, multiset<string>> m;
    
    for(auto t : tickets)
        m[t[0]].insert(t[1]);
    
    vector<string> answer = {"ICN"};
    
    return fly(m, answer, tickets.size() + 1);
}