#include<stdio.h>
long long int phi[2002];
int main(int argc, char *argv[])
{
    int i,j,N=2000,n;
    for(i=2;i<=N;i++)
    phi[i]=i;
    for(i=2;i<=N;i++)
    {
                     if(phi[i]==i)
                     for(j=i;j<=N;j=j+i)
                     phi[j]=(phi[j]/i)*(i-1);
    }
    scanf("%d",&n);
    printf("%lld\n",phi[phi[n]]);
    return 0;
}
