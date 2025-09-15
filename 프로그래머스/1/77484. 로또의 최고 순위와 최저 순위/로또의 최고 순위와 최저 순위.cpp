#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int best, worst;
    
    best = worst = 0;
   
    for(auto l : lottos){
        
        if (l == 0){
            best++;
            continue;
        }
        auto it = find(win_nums.begin(), win_nums.end(), l);
        if (it != win_nums.end()){
            best++;
            worst++;
        }
    }
    
    best = best < 2 ? 6 : (7 - best);
    worst = worst < 2 ? 6 : (7 - worst);

    answer.push_back(best);
    answer.push_back(worst);
    
    return answer;
}