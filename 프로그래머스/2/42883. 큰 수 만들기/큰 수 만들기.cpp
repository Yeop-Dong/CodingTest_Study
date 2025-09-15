#include <string>
#include <vector>
#include <algorithm>
using namespace std;


string solution(string number, int k) {
    string answer = "";
   
    
    int max = 0;
    for(int i = 0; i < number.size() - k; i++){
        
        for(int j = max; j <= k + i; j++){
            if(number[max] < number[j])
                max = j;
        }
        answer += number[max++];
    }
    
    return answer;
}