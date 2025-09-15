#include <stdio.h>

int main(void) {
	int C;
	long long Dp[101] = { 1, 1, 1, 1, 2, 2, };

	scanf("%d", &C);

	for (int i = 6; i <= 100; i++)
		Dp[i] = Dp[i - 1] + Dp[i - 5];

	while (C--) {
		int n;
		scanf("%d", &n);
		printf("%lld\n", Dp[n]);
	}

}