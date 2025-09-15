#include <string>
#include <vector>
#include <iostream>

using namespace std;
typedef vector<vector<int>> key_type;

key_type rotate(key_type key){
    
    int s = key.size();
    
    vector<vector<int>> key_r(s, vector<int>(s, 0));
    int k = 0;
    for(int j = 0; j < s; j++){
        for(int i = s - 1; i >= 0; i--){
            key_r[k / s][k % s] = key[i][j];
            k++;
        }
    }
    
    return key_r;
}

bool fit(key_type key, key_type lock, pair<int, int> offset){
    auto [y, x] = offset;
    int ls = lock.size(), ks = key.size();
    for(int i = 0; i + y < ls && i < ks; i++){
        if (i + y < 0) continue;
        for(int j = 0; j + x < ls && j < ks; j++){
            if (j + x < 0) continue;
            lock[i+y][j+x] ^= key[i][j];
        }
    }
    
    for(auto l : lock)
        for(auto i : l)
            if (i == 0)
                return false;

    return true;
}
bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    vector<key_type> keys;
    
    keys.push_back(key);
    for(int i = 0; i < 3; i++){
        key = rotate(key);
        keys.push_back(key);
    }
    
    
    int ks, ls;
    ks = key.size();
    ls = lock.size();
    int start = 1 - ks;
    for(int y = start; y < ls; y++){
        for(int x = start; x < ls; x++){
            int i = 0;
            for(auto k : keys){
                if (fit(k, lock, {y, x}))
                    return true;
            }
        }
    }
    
    return false;
}