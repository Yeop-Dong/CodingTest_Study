#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int** calclcs(string x, string y) {
	x = "0" + x;
	y = "0" + y;

	int len1 = x.length(), len2 = y.length();
	int** lcs = new int* [len1];
	for (int i = 0; i < len1; i++) {
		lcs[i] = new int[len2];
		memset(lcs[i], 0, sizeof(int) * len2);
	}


	for (int i = 0; i < len1; i++) {
		for (int j = 0; j < len2; j++) {
			if (!i || !j)
				lcs[i][j] = 0;
			else if (x[i] == y[j])
				lcs[i][j] = lcs[i - 1][j - 1] + 1;
			else {
				if (lcs[i - 1][j] > lcs[i][j - 1])
					lcs[i][j] = lcs[i - 1][j];
				else
					lcs[i][j] = lcs[i][j - 1];
			}
		}
	}

	return lcs;
}

int main(void){
    string a, b;
    
    cin >> a;
    cin >> b;

    int ** lcs = calclcs(a, b);
    cout << lcs[a.length()][b.length()];
}