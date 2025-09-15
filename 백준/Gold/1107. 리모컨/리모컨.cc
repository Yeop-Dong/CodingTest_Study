#include <iostream>
#include <set>
#include <string>
using namespace std;


int ch = 100;
int n, m;
int tmp;
bool btn_broken[10] = { false };


bool ch_possible(int ch) {
	string str_ch = to_string(ch);
	for (auto c : str_ch) {
		if (btn_broken[c - '0'])
			return false;
	}
	return true;
}

int main(void) {
	
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		cin >> tmp;
		btn_broken[tmp] = true;
	}
	
	int nearest_diff = 1000000;

	for (int i = 0; i <= 1000000; i++) {
		if (ch_possible(i)) {
			int diff = abs(n - i) + to_string(i).length();
			if (nearest_diff > diff) {
				nearest_diff = diff;
			}
		}
	}

	int diff1 = nearest_diff;
	int diff2 = abs(100 - n);

	cout << (diff1 < diff2 ? diff1 : diff2);
	
	return 0;
}