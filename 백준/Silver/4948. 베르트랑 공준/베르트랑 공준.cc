#include <iostream>
#include <list>
#include <string.h>
#include <math.h>
using namespace std;


int main()
{
	int a;

	
	a = 123456;
	bool *arr= new bool[a*2+1];
	memset(arr, false, sizeof(bool) * (a*2+1));

	for(int i = 2; i<= a*2; i++)
	{
		if (i * i > a*2) break;
		for(long long j = i*i; j <= a*2; j+=i)
		{
			arr[j] = true;
		}

	}


	while(1)
	{
		scanf("%d", &a);
		if (a==0) break;
		int cnt = 0;
		for(int i = a+1; i <= a*2; i++)
		{
			if (!arr[i]) cnt++;
		}
		
		printf("%d\n", cnt);
	}


	return 0;
}