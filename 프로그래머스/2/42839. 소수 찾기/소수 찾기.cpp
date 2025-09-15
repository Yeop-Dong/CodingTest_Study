#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <set>

using namespace std;

bool eratos[10000000];

void calc_eratos(){
    eratos[0] = eratos[1] = true;
    for(int i = 2; i < sqrt(10000000); i++){
        for(int j = 2; i * j < 10000000; j++){
            eratos[i*j] = true;
        }
    }
}
bool isPrime(int n){
    return !eratos[n];
}

set<int> cntRecur(string pick, string numbers){
        
    set<int> result;
    // not pick
    if (pick.size() != 0)
        if (isPrime(stoi(pick))){
            result.insert(stoi(pick));
        }
    
    // pick one more
    for(int i = 0; i < numbers.size(); i++){
        string left = numbers;
        left.erase(left.begin() + i);
        
        auto rec = cntRecur(pick + numbers[i], left);
        for(auto r : rec){
            result.insert(r);
        }
    }
    
    return result;
}

int solution(string numbers) {
    int answer = 0;
    calc_eratos();
    auto res = cntRecur("", numbers);
    
    answer = res.size();
    
    return answer;
}