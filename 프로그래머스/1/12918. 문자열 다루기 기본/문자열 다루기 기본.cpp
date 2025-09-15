#include <string>
#include <vector>

using namespace std;

bool solution(string s) {
    
    if (s.size() != 4 && s.size() != 6) return false;
    
    for (auto c : s){
        if ('0' <= c && c <= '9') continue;
        return false;
    }
    
    
    return true;
}