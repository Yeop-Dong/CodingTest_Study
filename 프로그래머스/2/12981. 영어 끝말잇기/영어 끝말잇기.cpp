#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    map<string, int> db;
    string save = words[0];
    db[words[0]]++;
    
    for(int i = 1; i < words.size(); i++){
        
        db[words[i]]++;
        if (db[words[i]] > 1 || save.back() != words[i].front() || words[i].size() == 1) {
            answer.push_back(i % n + 1);
            answer.push_back(i / n + 1);
            return answer;
        }
        save = words[i];
    }
    
    return vector<int>({0, 0});
}