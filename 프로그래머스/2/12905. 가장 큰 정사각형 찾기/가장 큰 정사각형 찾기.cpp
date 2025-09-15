#include <iostream>
#include<vector>
using namespace std;

int solution(vector<vector<int>> board)
{
    int answer = 1234;
    int r = board.size(), c = board[0].size();
    vector<vector<int>> save(r, vector<int>(c, 0));
    
    int max = 0;
    for(int i = r - 1; i >= 0; i--){
        for(int j = c - 1; j >= 0; j--){
            if (!board[i][j]) continue;
            
            save[i][j] = 1;
            int min = 1001;
            if (i + 1 < r && j + 1 < c){
                if (min > save[i+1][j]) min = save[i+1][j];
                if (min > save[i][j+1]) min = save[i][j+1];
                if (min > save[i+1][j+1]) min = save[i+1][j+1];
                save[i][j] += min;
            }
            if (max < save[i][j]) 
                max = save[i][j];
        }
    }

    return max * max;
}