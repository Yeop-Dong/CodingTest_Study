#include <stdio.h>

int main()
{
	int n;
	int temp;
	int i =0;

	scanf("%d", &n);
	temp = n;
	while (1)
	{
		if (temp % 5 == 0) break;
		temp -= 3;
		i++;
		if (temp < 0) i = -1;
	}

	if (i == -1) printf("%d", i);
	else printf("%d", temp/5+i);

	return 0;
}