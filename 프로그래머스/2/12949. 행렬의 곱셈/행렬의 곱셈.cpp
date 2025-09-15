#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer;
    
    for(int i1 = 0; i1 < arr1.size(); i1++){
        answer.push_back(vector<int>());
        for(int j1 = 0; j1 < arr2[0].size(); j1++){
            int tmp = 0;
            for(int k = 0; k < arr2.size(); k++){
                tmp += arr1[i1][k] * arr2[k][j1];
            }
            answer[i1].push_back(tmp);
        }
    }
    
    return answer;
}