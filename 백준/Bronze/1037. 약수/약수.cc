#include <bits/stdc++.h>

using namespace std;

int main(void){
	int n;
	int m, M;

	cin >> n;

	m = 1000001;
	M = 1;
	for(int i = 0; i < n; i++){
		int tmp;
		cin >> tmp;
		m = m > tmp ? tmp : m;
		M = M < tmp ? tmp : M;
	}

	cout << m * M << endl;

	return 0;
}
