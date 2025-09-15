#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

string ott(int n, int d){
    if (n <= 0) return "";
    
    string last;
    int nd = d * 3;
    int left = (n-1) % nd / d;
    
    switch(left){
        case 0:
            last = "1";
            break;
        case 1:
            last = "2";
            break;
        case 2:
            last = "4";
            break;
    }
    
    return ott(n - nd, nd) + last;
    
    
}

string solution(int n) {
    string answer = "";
    
    answer = ott(n, 1);
    
    return answer;
}