#include <stdio.h>

void rangeSubsetSum(int set[], int n, int a, int b, int total, int * cnt) {
	
	if (n == 0) {
		if (a <= total && total <= b) (*cnt)++;

		return;
	}

	rangeSubsetSum(set + 1, n - 1, a, b, total + set[0], cnt);	// 선택
	rangeSubsetSum(set + 1, n - 1, a, b, total, cnt);			// 선택 x
}
int main(void) {
	int n, a, b, cnt = 0;
	int x[20];

	scanf("%d %d", &n, &a);

	b = a;
	for(int i = 0; i < n; i++) {
		scanf("%d", x+i);
	}

	rangeSubsetSum(x, n, a, b, 0, &cnt);

	if (a == 0) cnt--;
	printf("%d\n", cnt);
}