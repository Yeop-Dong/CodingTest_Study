#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> works) {
    long long answer = 0;
    make_heap(works.begin(), works.end());
    
    for(auto i = 0; i < n; i++){
        pop_heap(works.begin(), works.end());
        works.back()--;
        push_heap(works.begin(), works.end());
    }
    
    for(auto w : works) {
        if (w < 0) return 0;
        answer += w * w;
    }
    return answer;
}