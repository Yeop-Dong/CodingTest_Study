#include <string>
#include <vector>
#include <tuple>
using namespace std;

int range_check(vector<vector<int>> &qtree, tuple<int, int, int> qinfo){
    int y, x, len;
    tie(y, x, len) = qinfo;
    int comp = qtree[y][x];
    
    for(int i = y; i < y + len; i++)
        for(int j = x; j < x + len; j++)
            if (comp != qtree[i][j])
                return -1;
        
    return comp;
}

vector<int> rqtree(vector<vector<int>> &qtree, tuple<int, int, int> qinfo){
    
    int y, x, len;
    tie(y, x, len) = qinfo;
    
    int cnt1 = 0, cnt0 = 0;
    int zip = range_check(qtree, qinfo);
    
    len /= 2;
    if (zip == -1)
        for(int i = 0; i < 2; i++)
            for(int j = 0; j < 2; j++){
                auto res_ij = rqtree(qtree, {y + i * len, x + j * len, len});
                cnt0 += res_ij[0];
                cnt1 += res_ij[1];
            }
    else if (zip == 0)
        cnt0++;
    else
        cnt1++;
    
    return vector<int>({cnt0, cnt1});
}

vector<int> solution(vector<vector<int>> arr) {
    vector<int> answer;
    
    answer = rqtree(arr, {0, 0, arr.size()});
    
    return answer;
}