#include <string>
#include <vector>

using namespace std;

vector<vector<int>> answer;
void rhanoi(int n, int from, int aux, int to){
    if (n == 0) return;
    
    rhanoi(n-1, from, to, aux);
    answer.push_back({from, to});
    rhanoi(n -1, aux, from, to);
    
}
vector<vector<int>> solution(int n) {
    rhanoi(n, 1, 2, 3);
    return answer;
}