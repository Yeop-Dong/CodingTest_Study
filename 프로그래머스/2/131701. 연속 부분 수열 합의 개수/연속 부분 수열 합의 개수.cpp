#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(vector<int> elements) {
    int s = elements.size();
    
    vector<int> acc(s, 0);
    set<int> ss_sum;
    
    for(int i = 0; i < s; i++){
        for(int j = s - 1; j >= 0; j--){
            acc[j] += elements[(s+j-i)%s];
            ss_sum.insert(acc[j]);
        }
    }
    
    return ss_sum.size();
}