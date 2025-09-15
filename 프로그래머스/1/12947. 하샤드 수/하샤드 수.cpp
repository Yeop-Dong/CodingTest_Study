#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    int sum = 0;
    for(int j = x; j > 0; j /= 10){
        sum += j % 10;
    }
    return x % sum == 0;
}