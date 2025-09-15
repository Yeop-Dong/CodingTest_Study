#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <sstream>


using namespace std;

vector<string> split(string input, char delimiter) {
    vector<string> result;
    stringstream ss(input);
    string tmp;
 
    while (getline(ss, tmp, delimiter)) result.push_back(tmp);
 
    return result;
}

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer(id_list.size(), 0);
    vector<int> reported_cnt(id_list.size(), 0);
    
    map<string, int> id_idx;
    vector<pair<int, int>> report_idx;
    
    for(int i = 0; i < id_list.size(); i++){
        id_idx[id_list[i]] = i;
    }
    
    sort(report.begin(), report.end());
    report.erase(unique(report.begin(), report.end()), report.end());
    
    for(auto r: report){
        vector<string> r_split = split(r, ' ');
        int reporter = id_idx[r_split[0]], reported = id_idx[r_split[1]];
        
        report_idx.push_back({reporter, reported});
        reported_cnt[reported]++;
    }
    
    for(int i = 0; i < id_list.size(); i++){
        if (reported_cnt[i] >= k){
            for(auto r : report_idx){
                if (r.second == id_idx[id_list[i]])
                    answer[r.first]++;
            }
        }
    }
    
    return answer;
}