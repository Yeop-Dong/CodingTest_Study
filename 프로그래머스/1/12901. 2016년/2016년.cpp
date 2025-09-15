#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    string answer = "";
    vector<int> days{31,29,31,30,31,30,31,31,30,31,30,31};
    vector<string> dayname{"SUN", "MON", "TUE", "WED","THU", "FRI", "SAT"};
    int day = 5;
    for(int i = 1; i < a; i++){
        day += days[i-1];
    }
    day += b;
    day--;
    
    answer = dayname[day % 7];
    
    return answer;
}