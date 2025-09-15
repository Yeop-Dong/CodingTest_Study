#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <iostream>


using namespace std;

vector<string> solution(vector<string> record) {
    vector<string> answer;
    map<string, string> user;
    vector<pair<char, string>> uid_record;
    
    for(auto r : record){
        stringstream ss(r);
        string buf;
        vector<string> cmd;
        
        while(getline(ss, buf, ' ')) cmd.push_back(buf);
        
        if (cmd[0] == "Enter"){
            uid_record.push_back({'E', cmd[1]});
            user[cmd[1]] = cmd[2];
        }
        else if (cmd[0] == "Leave"){
            uid_record.push_back({'L', cmd[1]});
        }
        else if (cmd[0] == "Change"){
            user[cmd[1]] = cmd[2];
        }
        
    }
    
    for(auto r : uid_record){
        string line = "";
        char cmd = r.first;
        string uid = r.second;
        switch(cmd){
            case 'E':
                line = user[uid] +"님이 들어왔습니다.";
                break;
            case 'L':
                line = user[uid] +"님이 나갔습니다.";
                break;
        }
        
        answer.push_back(line);
    }
    
    
    return answer;
}