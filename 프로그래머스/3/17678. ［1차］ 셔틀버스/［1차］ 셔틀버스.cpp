#include <string>
#include <vector>
#include <algorithm>
using namespace std;

inline int time_to_min(string time){
    return stoi(time.substr(0, 2)) * 60 + stoi(time.substr(3, 2));
}
inline string min_to_time(int min){
    char buf[6];
    sprintf(buf, "%02d:%02d", min / 60, min % 60);
    return string(buf);
}
string solution(int n, int t, int m, vector<string> timetable) {
    string answer = "";
    int start_time = 9*60;
    vector<int> mintable;
    
    for(auto t : timetable)
        mintable.push_back(time_to_min(t));
    sort(mintable.begin(), mintable.end());
    
    
    int before = 0, corn;
    
    for(int i = 0; i < n; i++){
        int bus = start_time + (i * t);
        int cnt = 0;
        for(int k = before; k < mintable.size(); k++){
            if (mintable[k] > bus) break;
            
            before++;
            cnt++;
            if (cnt == m) break;
            
        }
        
        if (i == n-1){
            if (cnt == m) corn = mintable[before-1]-1;
            else corn = bus;
        }
    }
    
    return min_to_time(corn);
    
}