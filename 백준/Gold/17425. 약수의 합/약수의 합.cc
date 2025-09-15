#include <bits/stdc++.h>

using namespace std;

const int MAX = 1000000;
int main(void){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	vector<long long> f(MAX+1, 1);
	vector<long long> g(MAX+1, 0);
	for(int i = 2; i <= MAX; i++){
		for(int j = 1; i * j <= MAX; j++){
			f[i*j] += i;
		}
	}
	for(int i = 1; i <= MAX; i++)
		g[i] += g[i-1] + f[i];

	int n, T;
	long long ans = 0;
	cin>> T;
	while(T--){
		cin >> n;
		cout << g[n] << "\n";
	}
	

	return 0;
}
