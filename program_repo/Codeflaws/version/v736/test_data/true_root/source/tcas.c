#include<stdio.h>
int main(int argc, char *argv[])
{
	int gl,gr,bl,br,i,j,k,l;
	scanf("%d %d\n%d %d",&gl,&gr,&bl,&br);
	printf((gl>1)&&(br>=gl-1)&&(br<=gl+3)?"YES":((gr>1)&&(bl>=gr-1)&&(bl<=gr+3)?"YES":"NO"));
	return 0;
}