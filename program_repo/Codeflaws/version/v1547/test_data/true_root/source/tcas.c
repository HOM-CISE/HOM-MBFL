#include<stdio.h>
#include<math.h>
#define sc(x) scanf("%lld",&x)
#define pr(x) printf("%lld",x)
#define ll long long int
int main(int argc, char *argv[])
{
	ll n,a[5],i,p;
	char c;
	for(i=0;i<5;i++)
	{
		c=getchar();
		a[i]=c-'0';
	}
	n=10000*a[0]+1000*a[2]+100*a[4]+10*a[3]+a[1];
	p=1;
	for(i=0;i<5;i++)
	{
		p*=n;
		p%=100000;
	}
	pr(p);
	return 0;
}
