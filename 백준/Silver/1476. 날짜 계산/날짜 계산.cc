#include <iostream>

using namespace std;

int main(void) {
	int E, S, M;
	cin >> E >> S >> M;
	E--;
	S--;
	M--;
	int e, s, m;
	e = s = m = 0;
	for (int i = 1; ; i++) {
		if (e == E && s == S && m == M) {
			cout << i << endl;
			return 0;
		}
		e = (e + 1) % 15;
		s = (s + 1) % 28;
		m = (m + 1) % 19;
	}
	return 0;
}