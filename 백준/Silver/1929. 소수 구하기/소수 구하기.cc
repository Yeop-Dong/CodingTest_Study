#include <iostream>
#include <list>
#include <string.h>
#include <math.h>
using namespace std;


int main()
{
	int a,b;
	scanf("%d %d", &a, &b);

	bool *arr= new bool[b+1];
	memset(arr, false, sizeof(bool) * (b+1));

	for(int i = 2; i<= b; i++)
	{
		if (i * i > b) break;
		for(long long j = i*i; j <= b; j+=i)
		{
			arr[j] = true;
		}
	}

	if (a == 1) a++;
	for(int i = a; i <= b; i++)
	{
		if (!arr[i]) printf("%d\n", i);
	}

	
}