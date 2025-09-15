#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    vector<queue<int>> bridge(bridge_length, queue<int>());
    queue<int> fin;
    int truck_cnt = truck_weights.size(), total_weight = 0;
    while(fin.size() < truck_cnt){
        
        if (bridge.back().size()){
            fin.push(bridge.back().front());
            total_weight -= bridge.back().front();
            bridge.back().pop();
        }
        
        for(int i = bridge.size() - 1; i >= 0; i--){
            if (bridge[i].size()){
                bridge[i+1].push(bridge[i].front());
                bridge[i].pop();
            }
        }
        
        if (truck_weights.size()){
            if (truck_weights[0] + total_weight <= weight){
                bridge[0].push(truck_weights[0]);
                total_weight += truck_weights[0];
                truck_weights.erase(truck_weights.begin());
            }
        }
        
        answer++;
       
    }
    return answer;
}