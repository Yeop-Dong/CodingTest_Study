#include <string>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    
    list<pair<int, int>> order;
    
    for(int i = 0; i < priorities.size(); i++)
        order.push_back({i, priorities[i]});
    
    while(!order.empty()){
        pair<int, int> now = order.front();
        order.pop_front();
        
        auto it = find_if(order.begin(), order.end(), [=](auto p)->bool{
            return p.second > now.second;
        });
        
        if (it != order.end())
            order.push_back(now);
        else{
            answer++;
            if (location == now.first)
                break;
        }
    }
    
    
    return answer;
}