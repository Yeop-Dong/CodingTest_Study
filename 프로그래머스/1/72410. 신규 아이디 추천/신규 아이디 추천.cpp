#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string new_id) {
    
    //1
    transform(new_id.begin(), new_id.end(), new_id.begin(), [](auto c) {
        return tolower(c);
        });
    
    //2
    new_id.erase(remove_if(new_id.begin(), new_id.end(), [](auto c){
        if ('a' <= c && c <= 'z')
            return false;
        if ('0' <= c && c <= '9')
            return false;
        if (c == '-' || c == '_' || c == '.')
            return false;
        return true;
    }), 
                 new_id.end());
    
    //3
    for(int i = 0; i < new_id.size(); i++){
        if (new_id[i] == '.'){
            int k = i+1;
            while(new_id[k++] == '.');
            if (k != i+2) new_id.erase(i, k-i-2);
        }
    }
    
    
    //4
    if (new_id[0] == '.') new_id.erase(new_id.begin() + 0);
    if (new_id[new_id.size() - 1] == '.') new_id.pop_back();
    
    //5
    if (new_id.empty()) new_id = "a";
    
    //6
    if (new_id.length() >= 16) new_id = new_id.substr(0, 15);
    if (new_id[new_id.size() - 1] == '.') new_id.pop_back();
    
    
    //7
    while(new_id.length() <= 2){
        new_id.push_back(new_id[new_id.size() - 1]);
    }
    
    return new_id;
}