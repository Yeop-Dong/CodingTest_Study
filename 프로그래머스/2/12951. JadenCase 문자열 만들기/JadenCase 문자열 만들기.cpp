#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s) {
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    for(int i = 0; i < s.size(); i++){
        if (i == 0 || s[i-1] == ' ')
            s[i] = toupper(s[i]);
    }
    return s;
}