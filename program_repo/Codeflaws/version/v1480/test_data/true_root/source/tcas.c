#include<stdio.h>
int main(int argc, char *argv[])
{
    long long n,i=1,k;
    scanf("%lld",&n);

    while(1)
    {
       n=n-i;
       if(n<=0) break;
       i++;
       k=n;
    }
    printf("%lld",k);
    return 0;
}
