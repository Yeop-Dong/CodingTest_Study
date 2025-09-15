#include <vector>
#include <algorithm>
#include<iostream>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    int cnt = nums.size() / 2;

    for(int i = 0; i < cnt; i++){
        int pick = nums[0];
        nums.erase(remove(nums.begin(), nums.end(), pick), nums.end());
        answer++;
    
        
        
        if (nums.size() == 0) break;
    }
    
    return answer;
}