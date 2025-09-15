using namespace std;

long long solution(int price, int money, int count)
{
    long long sum = money;
    
    for(int i = 1; i <= count; i++){
        sum -= (price * i);
    }
    
    if (sum > 0) return 0;
    return -1 * sum;
}