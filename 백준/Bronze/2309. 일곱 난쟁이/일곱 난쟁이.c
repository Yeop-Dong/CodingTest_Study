#include <stdio.h>
#include <stdlib.h>
#define TOTAL_HEIGHT 100
int compare(const void *first,const void *second)
{
	if (*(int*)first > *(int*)second)
		return 1;
	else if (*(int*)first < *(int*)second)
		return -1;
	else
		return 0;
}
int main()
{
	int h[9];
	int arr_len = sizeof(h) / sizeof(int);
	int pos1, pos2;
	int sum = 0;

	for (int i = 0; i < 9; i++)
	{
		scanf("%d", h + i);
		sum += h[i];
	}
	sum -= TOTAL_HEIGHT;
	qsort(h, arr_len, sizeof(int), compare);
	
	for (int i = 0; i < arr_len-1; i++)
	{
		for (int j = i+1; j < arr_len; j++)
		{
			if (h[i] + h[j] == sum)
			{
				pos1 = i;
				pos2 = j;
				goto output;

			}
		}
	}

output:

	for (int i = 0; i < 9; i++)
	{
		if (i == pos1 || i == pos2) continue;
		printf("%d\n", h[i]);
	}

	return 0;
}