#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    
    int idx = 0;
    for(auto &c : s){
        if (isblank(c)) idx = -1;
        else if (idx % 2 == 0) c = toupper(c);
        else c = tolower(c);
        
        idx++;
    }
    answer = s;
    
    return answer;
}