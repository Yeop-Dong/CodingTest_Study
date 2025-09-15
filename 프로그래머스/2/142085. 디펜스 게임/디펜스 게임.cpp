#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(int n, int k, vector<int> enemy) {
    
    if (enemy.size() <= k)
        return enemy.size();
    
    priority_queue< int, vector<int>, greater<int> > pq;

    int round = 0;
    for(auto e : enemy){
        pq.push(e);
        
        if (k < pq.size()){
            n -= pq.top();
            pq.pop();
        }
        if (n < 0)
            return round;
        round++;
    }
    
    return enemy.size();
    
}