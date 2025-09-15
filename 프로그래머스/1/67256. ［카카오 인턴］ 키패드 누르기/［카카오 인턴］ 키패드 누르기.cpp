#include <string>
#include <vector>
#include <cmath>
using namespace std;

int dist(pair<int,int> x, pair<int, int> y){
    return abs(x.first-y.first) + abs(x.second - y.second);
}
string solution(vector<int> numbers, string hand) {
    string answer = "";
    pair<int, int> lpos(0,0), rpos(0,2);
    vector<pair<int, int>> nums{ {0,1},{3,0},{3,1},{3,2},{2,0},{2,1},{2,2},{1,0},{1,1},{1,2} };
    
    for(auto n: numbers){
        if (n == 1 || n == 4 || n == 7) {
            lpos = nums[n];
            answer += 'L';
            continue;
        }
        if (n == 3 || n == 6 || n == 9) {
            rpos = nums[n];
            answer += 'R';
            continue;
        }
        
        int ldist = dist(lpos, nums[n]);
        int rdist = dist(rpos, nums[n]);
        
        if (ldist == rdist){
            if (hand == "right") {
                rpos = nums[n];
                answer += 'R';
            }
            else {
                lpos = nums[n];
                answer += 'L';
            }
            continue;
        }
        if (ldist > rdist){
            rpos = nums[n];
            answer += 'R';
        }
        else{
            lpos = nums[n];
            answer += 'L';
        }
        
    }
    
    
    return answer;
}