#include <stdio.h>
main(s){
	scanf("%d",&s);
	printf("%c",s>89?'A':(s>79?'B':(s>69?'C':(s>59?'D':'F'))));
}