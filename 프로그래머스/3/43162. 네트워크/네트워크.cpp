#include <string>
#include <vector>

using namespace std;

void dfs(vector<vector<int>> &computers, vector<bool> &visited, int i){
    
    visited[i] = true;
    
    for(int j = 0; j < computers.size(); j++){
        if (i == j) continue;    
        if (computers[i][j] && !visited[j]) 
            dfs(computers, visited, j);
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<bool> visited(computers.size(), false);
    
    while(true){
        int i = 0;
        for(i = 0; i < visited.size(); i++){
            if (!visited[i])
                break;
        }
        if (i == visited.size())
            break;
        
        dfs(computers, visited, i);
        answer++;
    }
    
    
    return answer;
}