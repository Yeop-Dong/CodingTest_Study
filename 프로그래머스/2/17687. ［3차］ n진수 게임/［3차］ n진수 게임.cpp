#include <string>
#include <vector>
#include <map>
#include <iostream>
using namespace std;

string solution(int n, int t, int m, int p) {
    string answer = "";
    map<int, char> nums;
    
    for(int i = 0; i < 10; i++)
        nums[i] = i + '0';
    for(int i = 0; i <= 6; i++)
        nums[i + 10] = i + 'A';
    
    int k = 0;
    for(int i = 0; answer.size() < t; i++){
        int tmp = i;
        string conv = "";
        do{
            conv = nums[tmp % n] + conv;
            tmp /= n;
        }while(tmp);
        
        for(auto c : conv){
            if (k % m == p - 1){
                answer += c;
                if (answer.size() == t) break;
            }
            k++;
        }
    }
    
    return answer;
}