#include <string>
#include <vector>
#include <set>
using namespace std;

bool check(string id, string query){
    if (id.size() != query.size())
        return false;
    
    for(int i = 0; i < id.size(); i++)
        if (id[i] != query[i] && query[i] != '*')
            return false;
    
    return true;
}

void combination(set<set<int>> &ban, vector<vector<int>> ban_cand, int i, set<int> cur){
    
    if (i == ban_cand.size()){
        if (ban.count(cur) == 0)
            ban.insert(cur);
        return;
    }
    
    for(auto b : ban_cand[i]){
        if (cur.count(b) > 0) continue;
        set<int> tmp(cur);
        tmp.insert(b);
        combination(ban, ban_cand, i+1, tmp);
    }
}
int solution(vector<string> user_id, vector<string> banned_id) {
    int answer = 0;
    vector<vector<int>> ban_cand;
    
    for(auto b : banned_id){
        ban_cand.push_back(vector<int>());
        for(int u = 0; u < user_id.size(); u++){
            if (check(user_id[u], b))
                ban_cand.back().push_back(u);
        }
    }
    
    set<set<int>> ban;
    combination(ban, ban_cand, 0, set<int>());
    
    return ban.size();
}