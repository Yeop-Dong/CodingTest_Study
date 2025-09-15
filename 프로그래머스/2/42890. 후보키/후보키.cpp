#include <string>
#include <vector>
#include <map>
#include <cmath>

using namespace std;


int solution(vector<vector<string>> relation) {
    int answer = 0;
    int col = relation[0].size(), row = relation.size();
    int mask_size = pow(2, col);
    map<string, int> key;
    vector<int> cand;

    int mask, r, c;
    
    for(mask = 1; mask < mask_size; mask++){
        for(r = 0; r < row; r++){
            string tmp = "";
            for(c = 0; c < col; c++){
                tmp += mask & (1 << (col - c - 1)) ? relation[r][c] + " " : "- ";
            }
            key[tmp]++;
            if (key[tmp] > 1)
                break;
        }
        if (r == row)
            cand.push_back(mask);
    }
    
    for(int i = 0; i < cand.size(); i++){
        for(int j = i+1; j < cand.size(); j++){
            if ((cand[i] & cand[j]) == cand[i]) {
                cand.erase(cand.begin() + j);
                j--;
            }
        }
    }
    
    answer = cand.size();
    
    return answer;
}