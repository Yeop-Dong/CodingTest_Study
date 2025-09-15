#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;

    for(int i = 0; i < arr.size(); i++){
        int tmp = arr[i];
        answer.push_back(tmp);
        for (i++; i < arr.size() && arr[i] == tmp; i++);
        i--;
    }
    return answer;
}