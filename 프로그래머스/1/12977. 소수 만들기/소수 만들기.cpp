#include <vector>
#include <iostream>
#include <cmath>
#include <algorithm>


using namespace std;

bool eratos[50001];

void calc_prime(int num){
    eratos[1] = true;
    for(int i = 2; i <= sqrt(num); i++){
        for(int j = 2; i * j <= num; j++){
            eratos[i * j] = true;
        }
    }
}

int solution(vector<int> nums) {
    int answer = 0;
    
    calc_prime(50000);
    
    for(int i = 0; i < nums.size(); i++){
        for(int j = i+1; j < nums.size(); j++){
            for(int k = j+1; k < nums.size(); k++){
                int num = nums[i] + nums[j] + nums[k];
                if (!eratos[num]) answer++;
            }
        }
    }
    
    return answer;
}