#include <string>
#include <vector>
#include <map>
#include <tuple>
#include <algorithm>

using namespace std;

bool reachable(pair<int, int> a, pair<int, int> b, vector<string> &board){
    // ay <= by 전제
    auto [ay, ax] = a;
    auto [by, bx] = b;
    
    auto [min_x, max_x] = minmax(ax, bx);
    
    int y, x;
    // case 1 vertical first
    bool can_reach = true;
    for(y = ay; y <= by && can_reach; y++)
        if (board[y][ax] != '.' && board[y][ax] != board[ay][ax])
            can_reach = false;
    for(x = min_x; x <= max_x && can_reach; x++)
        if (board[by][x] != '.' && board[by][x] != board[ay][ax])
            can_reach = false;
    if (can_reach) 
        return true;
    
    // case 2 horizontal first
    can_reach = true;
    for(x = min_x; x <= max_x && can_reach; x++)
        if (board[ay][x] != '.' && board[ay][x] != board[ay][ax])
            can_reach = false;
    for(y = ay; y <= by && can_reach; y++)
        if (board[y][bx] != '.' && board[y][bx] != board[ay][ax])
            can_reach = false;
    
    return can_reach;
}

string solution(int m, int n, vector<string> board) {
    string answer = "";
    
    bool find;
    map<char, tuple<int, int, int, int>> s;
    
    for(int y = 0; y < m; y++){
        for(int x = 0; x < n; x++){
            if (board[y][x] == '.' || board[y][x] == '*')
                continue;
            s[board[y][x]] = {0, 0, 0, 0};        
        }
    }
    
    int cnt = s.size();
    
    do {
        s.clear();
        for(int y = 0; y < m; y++){
            for(int x = 0; x < n; x++){
                if (board[y][x] == '.' || board[y][x] == '*')
                    continue;
                for(int k = y * n + x + 1; k < m * n; k++)
                    if (board[y][x] == board[k / n][k % n]){
                        if (reachable({y, x}, {k / n, k % n}, board))
                            s[board[y][x]] = {y, x, k / n, k % n};
                        break;
                    }
            }
        }
        
        if (s.size()){
            auto c = s.begin()->first;
            auto [ay, ax, by, bx] = s.begin()->second;
            answer += c;
            board[ay][ax] = board[by][bx] = '.';
        }
    }while(s.size());
    
    if (answer.size() < cnt)
        answer = "IMPOSSIBLE";
    return answer;
}