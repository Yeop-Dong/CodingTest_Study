#include <bits/stdc++.h>

using namespace std;

int main(void){
    int n;

    while(cin >> n){
        long long div = 1;
        int cnt;
        for(cnt = 1; div % n ; cnt++){
            div = div * 10 + 1;
            div %= n;
        }
        cout << cnt << endl;
    }

    return 0;
}
