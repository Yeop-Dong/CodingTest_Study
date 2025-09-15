#include <string>
#include <vector>
#include <tuple>
#include <algorithm>
#include <iostream>

using namespace std;

int time_to_ms(string t){
    int h = stoi(t.substr(11, 2));
    int m = stoi(t.substr(14, 2));
    double s = stod(t.substr(17, 6));
    s += h * 60 * 60;
    s += m * 60;
    
    return static_cast<int>(s * 1000);
}

int s_to_ms(string s){
    return static_cast<int>( stod(s.substr(0, s.find('s'))) * 1000);
}


int solution(vector<string> lines) {
    
    vector<tuple<char, int, int>> log;
    
    for(int i = 0; i < lines.size(); i++){
        int e = time_to_ms(lines[i]);
        int s = e - s_to_ms(lines[i].substr(24)) + 1;
        log.push_back({'S', i, s});
        log.push_back({'E', i, e});
    }
    
    sort(log.begin(), log.end(), [](auto l, auto r)->bool{
       if (get<2>(l) == get<2>(r))
           return get<0>(l) > get<0>(r);
        return get<2>(l) < get<2>(r);
    });
    
    vector<int> q;
    int max = 0;
    
    for(auto [cmd, num, time] : log){
        int s = time - 1000, e = time;
        auto time_cmp = [](tuple<char, int, int> l, tuple<char, int, int> t){ return get<2>(l) < get<2>(t); };
        auto sit = upper_bound(log.begin(), log.end(), make_tuple(0, 0, s), time_cmp);
        auto eit = lower_bound(log.begin(), log.end(), make_tuple(0, 0, e), time_cmp);
        
        int cnt = 0;
        while(sit != eit){
            if (get<0>(*sit) == 'E'){
                cnt++;
            }
            sit++;
        }
        
        if (cmd == 'S'){
            q.push_back(num);
        }
        else if (cmd == 'E'){
            auto qit = find(q.begin(), q.end(), num);
            if (qit != q.end()) q.erase(qit);
        }
        
        if (max < q.size() + cnt)
            max = q.size() + cnt;
    }
    
    
    return max;
}