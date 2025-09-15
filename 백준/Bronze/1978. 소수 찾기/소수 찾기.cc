#include <bits/stdc++.h>

using namespace std;

int main(void){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	const int M = 1000;
	vector<bool> e(M+1, true);

	e[1] = false;
	for(int i = 2; i <= M; i++){
		for (int j = 2; i * j <= M; j++)
			e[i * j] = false;
	}

	int n, t, ans = 0;
	cin >> n;
	while(n--){
		cin >> t;
		if (e[t]) ans++;
	}
	cout << ans << endl;
	return 0;
}
