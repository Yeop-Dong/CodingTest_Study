#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(string s) {
    int answer = 0;
    
    map<string, string> nummap = {
        {"zero", "0"},
        {"one", "1"},
        {"two", "2"},
        {"three", "3"},
        {"four", "4"},
        {"five", "5"},
        {"six", "6"},
        {"seven", "7"},
        {"eight", "8"},
        {"nine", "9"}
    };
    
    for(auto [eng, num] : nummap){
        int pos = 0;
        while(1){
            pos = s.find(eng, pos);
            if (pos == string::npos)
                break;
            s.replace(pos, eng.size(), num);
        }
    }
    
    answer = stoi(s);
    return answer;
}