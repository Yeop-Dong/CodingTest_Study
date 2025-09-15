#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>

using namespace std;

vector<int> solution(vector<string> info, vector<string> query) {
    vector<int> answer;
    
    vector<string> cat;
    map<string, vector<int>> db;
    
    for(auto in : info){
        stringstream ss(in);
        vector<string> data(4);
        int score;
        for(auto &d : data)
            ss >> d;
        ss >> score;
        
        for(int i = 0; i < 16; i++){
            string tmp = "";
            for(int j = 0; j < 4; j++){
                tmp += i & (1 << j) ? data[j] + "" : "-";
                if (j != 3) tmp += " and ";
            }
            if(db.count(tmp))
                db[tmp].push_back(score);
            else
                db[tmp] = vector<int>({score});
        }
    }
    
    for(auto &[key, l] : db)
        sort(l.begin(), l.end());

    for(auto q : query){
        int pos = q.rfind(" ");
        string key = q.substr(0, pos);
        int score = stoi(q.substr(pos));
        
        vector<int> l = db[key];
        answer.push_back( l.end() - lower_bound(l.begin(), l.end(), score) );
    }
   
    
    return answer;
}