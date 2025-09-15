#include <string>
#include <vector>
#include <tuple>
#include <iostream>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> files) {
    vector<string> answer;
    // head, num, tail, original
    vector<tuple<string, int, string, string>> db;
    
    for(auto f : files){
        int first, second;
        first = second = -1;
        for(int i = 0; i < f.size(); i++){
            if ('0' <= f[i] && f[i] <= '9'){
                if (first == -1)
                    first = i;
            }
            else if (first != -1){
                second = i - 1;
                break;
            }
        }
        
        string head, tail;
        int num;
        
        head = f.substr(0, first);
        transform(head.begin(), head.end(), head.begin(), ::tolower);
        num = stoi(f.substr(first, second));
        tail = f.substr(second + 1);
        
        db.push_back({head, num, tail, f});
    }
    
    stable_sort(db.begin(), db.end(), [](auto l, auto r)->bool{
        return get<0>(l) == get<0>(r) ? get<1>(l) < get<1>(r) : get<0>(l) < get<0>(r);
    });
    
    for(auto d : db){
        answer.push_back(get<3>(d));
    }
    return answer;
}