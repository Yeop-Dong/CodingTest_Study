#include <vector>
#include <functional>

using namespace std;

int MOD = 20170805;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int m, int n, vector<vector<int>> city_map) {
    int answer = 0;
    const int right = 0, down = 1;
    MOD = 20170805;
    vector<tuple<int, int, int>> delta = {{right, 0, 1}, {down, 1, 0}};
    vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>(2, -1)));
    function<int(int, int, int)> dfs = [&](int y, int x, int dir_prev)->int{
        if (y >= m || x >= n)
            return 0;
        if (y == m - 1 && x == n - 1)
            return 1;
        if (dp[y][x][dir_prev] != -1)
            return dp[y][x][dir_prev];
        
        int sum = 0;
        for(auto [dir, dy, dx] : delta){
            auto [ny, nx] = pair(y + dy, x + dx);
            if (city_map[y][x] == 0 || (city_map[y][x] == 2 && dir == dir_prev))
                sum += dfs(ny, nx, dir) % MOD;
        }
        dp[y][x][dir_prev] = sum % MOD;
        
        return dp[y][x][dir_prev];
    };
    
    return dfs(0, 0, 0);
}