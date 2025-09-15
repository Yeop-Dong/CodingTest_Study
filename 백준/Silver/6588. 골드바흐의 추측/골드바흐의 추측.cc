#include <bits/stdc++.h>

using namespace std;

int main(void){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	const int MAX = 1000000;

	vector<bool> e(MAX + 1, true);
	e[1] = false;
	for(int i = 2; i <= MAX; i++){
		for(int j = 2; i * j <= MAX; j++){
			e[i * j] = false;
		}
	}
	while(true){
		int n;
		cin >> n;
		if (n == 0)
			break;
		int i;
		for(i = 3; i <= n; i+=2){
			if (e[i] && e[n - i])
				break;
		}
		if (i == n)
			printf("Goldbach\'s conjecture is wrong\n");
		else
			printf("%d = %d + %d\n", n, i, n-i);
		
	}
}
