#include <string>
#include <vector>

using namespace std;

string bin(int x, int meter){
    if (meter == 0) return "";
    return bin(x/2, meter-1) + (x%2 ? "#" : " ");
}

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    for(int i = 0; i < n; i++){
        answer.push_back(bin(arr1[i] | arr2[i], n));
    }
    
    return answer;
}