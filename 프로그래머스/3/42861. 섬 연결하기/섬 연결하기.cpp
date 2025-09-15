#include <string>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    vector<int> sack(n);
    for(auto i = 0; i < n; i++){
        sack[i] = i;
    }
    
    sort(costs.begin(), costs.end(), [](auto a, auto b)->bool{
        return a[2] < b[2];
    });
    
    for(auto c : costs){
        auto [v1, v2, w] = tuple(c[0], c[1], c[2]);
        int p1 = sack[v1];
        int p2 = sack[v2];
        if (p1 == p2)
            continue;
        if (p1 > p2)
            swap(p1, p2);
        for(auto &s : sack){
            if (s == p2)
                s = p1;
        }
        answer += w;
    }
    
    return answer;
}