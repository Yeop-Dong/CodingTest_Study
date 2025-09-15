#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b, vector<int> g, vector<int> s, vector<int> w, vector<int> t) {
    long long answer = 4e14;
    long long left = 0, right = 4e14;
    long long mid;
    long long gold, silver, total;
    
    while(left <= right){
        mid = (left + right) / 2;
        gold = silver = total = 0;
        
        for(int i = 0; i < g.size(); i++){
            long long cnt = mid / (t[i] * 2);
            if (mid % (t[i] * 2) >= t[i]) cnt++;
            long long move = cnt * w[i];
            
            gold += (g[i] < move ? g[i] : move);
            silver += (s[i] < move ? s[i] : move);
            total += (g[i] + s[i] < move ? g[i] + s[i] : move);
        }
        
        if (gold >= a && silver >= b && total >= a + b){
            right = mid - 1;
            answer = min(mid, answer);
        }
        else
            left = mid + 1; 
    }

    return answer;
}