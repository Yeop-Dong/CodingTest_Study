#include <string>
#include <vector>

using namespace std;

long long seq[200];
long long acc[200];

vector<double> solution(int k, vector<vector<int>> ranges) {
    vector<double> answer;
    
    seq[0] = k;
    int i;
    for(i = 1; i < 200; i++){
        if (k % 2 == 0) k /= 2;
        else k = k * 3 + 1;
        seq[i] = k;
        acc[i] = seq[i-1] + seq[i] + acc[i-1];
        if (k == 1)
            break;
    }
    for(auto r : ranges){
        int s, e;
        s = r[0];
        e = i + r[1];
        if (s > e)
            answer.push_back(-1.0);
        else
            answer.push_back((acc[e] - acc[s])/2.0);
    }
    
    return answer;
}