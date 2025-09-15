#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    
    int time = 0, now = 0;
    
    sort(jobs.begin(), jobs.end());
    struct cmp{
        bool operator()(vector<int> l, vector<int> r){
            return l[1] > r[1];
        }
    };
    
    priority_queue<vector<int>, vector<vector<int>>, cmp> pq;
    
    while(now < jobs.size() || !pq.empty()){
        if (now < jobs.size() && jobs[now][0] <= time){
            pq.push(jobs[now++]);
            continue;
        }
        if(!pq.empty()){
            time += pq.top()[1];
            answer += time - pq.top()[0];
            pq.pop();
        }
        else
            time = jobs[now][0];
    }
    
    return answer / jobs.size();
}