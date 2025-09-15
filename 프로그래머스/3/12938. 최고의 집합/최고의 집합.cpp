#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int s) {
    vector<int> answer;
    
    for(auto i = 0; i < n; i++){
        if (s / n == 0)
            continue;
        answer.push_back(s / n);
    }
    if (answer.size() == 0)
        return vector<int>({-1});
    
    for(auto i = 0; i < s % n; i++){
        answer[answer.size() - 1 - i]++;
    }
    return answer;
}