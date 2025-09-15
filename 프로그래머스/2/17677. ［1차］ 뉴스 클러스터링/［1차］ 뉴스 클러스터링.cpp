#include <string>
#include <map>
#include <algorithm>
#include <iostream>



using namespace std;

map<string, int> cntPair(string s){
    map<string, int> cnts;
    for(int i = 0; i < s.size()-1; i++){
        string e = s.substr(i, 2);
        if (isalpha(e[0]) && isalpha(e[1]))
            cnts[e]++;    
    }
    return cnts;
}

int weight(map<string, int> a){
    int sum = 0;
    for (auto [str, cnt] : a){
        sum += cnt;
    }
    return sum;
}

map<string, int> intersection(map<string, int> a, map<string, int> b){
    map<string, int> c;
    for(auto [str, cnt] : a){
        auto it = b.find(str);
        if (it != b.end())
            c[str] = min(cnt, b[str]);
    }
    return c;
}

map<string, int> uni(map<string, int> a, map<string, int> b){
    map<string, int> c;
    for(auto [str, cnt] : a){
        auto it = b.find(str);
        if (it != b.end()){
            c[str] = max(cnt, b[str]);
            b.erase(str);
        }
        else
            c[str] = cnt;
    }
    for(auto [str, cnt] : b){
        c[str] = cnt;
    }
    return c;
}

int J_similarity(map<string, int> a, map<string, int> b){
    
    if (a.size() == 0 && b.size() == 0) 
        return 65536;
    
    int top, bot;
    
    top = weight(intersection(a, b));
    bot = weight(uni(a, b));
    
    cout << top << " " << bot << endl;
    
    return (int)(65536.0 * top / bot);
}
int solution(string str1, string str2) {
    
    int answer = 0;
    map<string, int> s1, s2;
        
    transform(str1.begin(), str1.end(), str1.begin(), ::tolower);
    transform(str2.begin(), str2.end(), str2.begin(), ::tolower);
    
    s1 = cntPair(str1);
    s2 = cntPair(str2);
    
    
    answer = J_similarity(s1, s2);
    
    return answer;
}