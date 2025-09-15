#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int gcd(int a, int b){
    if (a < b)
        swap(a, b);
    
    while(b > 0){
        int r = a % b;
        a = b;
        b = r;
    }
    
    return a;
}
int solution(vector<int> arr) {
    int answer = 1;
    
    for(int i = 1; i < arr.size(); i++){
        int g = gcd(arr[i-1], arr[i]);
        arr[i] = arr[i-1] * arr[i] / g;
    }
    
    return arr[arr.size()-1];
}