#include <bits/stdc++.h>

using namespace std;

int main(void){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int a, b;
	auto gcd = [](int x, int y)->int {
		int z;
		while(y){
			z = x % y;
			x = y;
			y = z;
		}
		return x;
	};
	cin >> a >> b;
	int g = gcd(a, b);
	cout << g << endl;
	cout << a * b / g << endl;
	return 0;
}
