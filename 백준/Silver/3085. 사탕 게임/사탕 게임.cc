#include <iostream>
#include <map>
using namespace std;

int n;
char candies[50][51];

int max_row() {

	int result = 0;
	for (int i = 0; i < n; i++) {
		int max = 1;
		int cnt = 1;
		char now = candies[i][0];
		for (int j = 1; j < n; j++) {
			if (now == candies[i][j]) {
				cnt++;
				if (max < cnt)
					max = cnt;
			}
			else {
				cnt = 1;
				now = candies[i][j];
			}
		}
		if (result < max)
			result = max;
	}
	return result;
}
int max_col() {

	int result = 0;
	for (int j = 0; j < n; j++) {
		int max = 1;
		int cnt = 1;
		char now = candies[0][j];
		for (int i = 1; i < n; i++) {
			if (now == candies[i][j]) {
				cnt++;
				if (max < cnt)
					max = cnt;
			}
			else {
				cnt = 1;
				now = candies[i][j];
			}
		}
		if (result < max)
			result = max;
	}
	return result;
}

int find_max() {
	int max = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n - 1; j++) {
			if (candies[i][j] == candies[i][j + 1])
				continue;

			swap(candies[i][j], candies[i][j + 1]);
			int r = max_row();
			if (max < r)
				max = r;
			int c = max_col();
			if (max < c)
				max = c;
			swap(candies[i][j], candies[i][j + 1]);
		}
	}
	for (int j = 0; j < n; j++) {
		for (int i = 0; i < n - 1; i++) {
			if (candies[i][j] == candies[i + 1][j])
				continue;
			swap(candies[i][j], candies[i + 1][j]);
			int r = max_row();
			if (max < r)
				max = r;
			int c = max_col();
			if (max < c)
				max = c;
			swap(candies[i][j], candies[i + 1][j]);
		}
	}
	return max;
}
int main() {

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> candies[i];
	}

	cout << find_max();
}