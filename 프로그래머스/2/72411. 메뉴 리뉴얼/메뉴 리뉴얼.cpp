#include <string>
#include <vector>
#include <map>
#include <algorithm>


using namespace std;

vector<string> combination(string select, string order, int course){
    
    if (course == 0){
        vector<string> end = { select };
        return end;
    }
    
    vector<string> res;
    
    for(int i = 0; i < order.size(); i++){
        string left_order = order;
        left_order = left_order.substr(i+1);
        
        string cur_select = select + order[i];
        
        vector<string> com = combination(cur_select, left_order, course-1);
        for (auto c : com){
            res.push_back(c);
        }
    }
    
    return res;
}

map<string, int> count_combination(vector<string> orders, int course){
    map<string, int> cnt_combs;
    map<string, int> res;
    for(auto o : orders){
        auto combs = combination("", o, course);
        
        for(auto c : combs){
            cnt_combs[c]++;
        }
    }

    int maxcnt = 0;
    for(auto [comb, cnt] : cnt_combs){
        if (cnt >= 2 && maxcnt < cnt){
            maxcnt = cnt;
        }
    }
    
    for(auto [comb, cnt] : cnt_combs){
        if (maxcnt == cnt){
            res[comb] = cnt;
        }
    }
    
    return res;

}
vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    
    for(auto &o : orders){
        sort(o.begin(), o.end());
    }
    
    for(auto c : course){
        auto res = count_combination(orders, c);
        for(auto [comb, cnt] : res){
            answer.push_back(comb);
        }
    }
    
    sort(answer.begin(), answer.end());
    return answer;
}