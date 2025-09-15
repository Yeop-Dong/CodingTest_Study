#include <bits/stdc++.h>

using namespace std;

int main(void){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int n;
	long long ans = 0;

	cin >> n;
	
	for(int i = 1; i <= n; i++){
		ans += (n / i) * i;
	}

	cout << ans << endl;

	return 0;
}
