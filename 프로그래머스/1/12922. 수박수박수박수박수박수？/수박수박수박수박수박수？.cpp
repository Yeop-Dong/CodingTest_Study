#include <string>
#include <vector>

using namespace std;

string solution(int n) {
    string answer = "";
    
    int sb = n / 2;
    for(int i = 0; i < sb; i++) answer += "수박";
    if (n%2) answer += "수";
    
    return answer;
}