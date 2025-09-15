#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <iostream>

using namespace std;

map<char, int> note = { {'A', 1}, {'B', 3}, {'C', 4},
                        {'D', 6}, {'E', 8}, {'F', 9}, {'G', 11} };

int time_to_min(string time){
    return stoi(time.substr(0, 2)) * 60 + stoi(time.substr(3, 2));
}

int time_diff(string start, string end){
    return time_to_min(end) - time_to_min(start);
}

vector<int> note_to_num(string m){
    vector<int> res;
    for(auto c : m){
        if (c == '#'){
            res.back()++;
        }
        else{
            res.push_back(note[c]);
        }
    }
    return res;
}

string solution(string m, vector<string> musicinfos) {
    string answer = "(None)";
    
    vector<int> m_note = note_to_num(m);
    
    int max = -1;
    for(auto in : musicinfos){
        stringstream ss(in);
        vector<string> info(4);
        
        string tmp;
        for(auto &i : info){
            getline(ss, tmp, ',');
            i = tmp;    
        }
        
        int min = time_diff(info[0], info[1]);
        vector<int> p_note = note_to_num(info[3]);

        if (p_note.size() > min)
            p_note.erase(p_note.begin() + min, p_note.end());
        else{
            vector<int> temp;
            for(int i = 0; i < min; i++)
                temp.push_back(p_note[i % p_note.size()]);
            p_note = temp;
        }
        
        for(int i = 0; i < p_note.size(); i++){
            if (p_note[i] != m_note[0]) continue;
            
            int j;
            for(j = 0; j < m_note.size(); j++){
                if (p_note[i + j] != m_note[j])
                    break;
            }
            if (j == m_note.size()){
                if (max < min){
                    max = min;
                    answer = info[2];
                }
            }
        }
        
    }
    
    return answer;
}