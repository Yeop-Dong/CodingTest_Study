#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    vector<int> bucket;
    
    for(auto m : moves){
        for (int d = 0; d < board.size(); d++){
            if (board[d][m-1]){
                
                bucket.push_back(board[d][m-1]);
                
                // bucket check
                
                if (bucket.size() > 1){
                    while(bucket[bucket.size()-1] == bucket[bucket.size()-2]){
                        bucket.pop_back();
                        bucket.pop_back();
                        answer+=2;
                    }
                }
                board[d][m-1] = 0;
                break;
                    
            }
        }
    }
    
    return answer;
}