#include <string>
#include <vector>

using namespace std;

int dfs(vector<int> numbers, int sum, int target){
    
    if (numbers.size() == 0) {
        if (sum == target) 
            return 1;
        else
            return 0;
    }
    
    int plus, minus;
    
    vector<int> next_numbers = numbers;
    next_numbers.erase(next_numbers.begin());
    
    plus = dfs(next_numbers, sum + numbers[0], target);
    minus = dfs(next_numbers, sum - numbers[0], target);
    
    return plus + minus;
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    
    answer = dfs(numbers, 0, target);
    
    return answer;
}