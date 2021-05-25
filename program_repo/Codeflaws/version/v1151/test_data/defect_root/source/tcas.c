#include <stdio.h>
#define m 1000000007
int main(int argc, char *argv[])
{
    long long a,b,c,n,ans;
    scanf("%lld %lld %lld",&a,&b,&n);
    c=(b-a);
    if(n%3==0)
    {
        if((n/3)%2==0)
            ans=-c;
        else
            ans=c;
    }
    else
    {
        if(n%3==1)
        {
            if((n/3)%2==0)
                ans=a;
            else
                ans=-a;
        }
        else if(n%3==2)
        {
            if((n/3)%2==0)
                ans=b;
            else
                ans=-b;         
        }
    }   
    printf("%lld",(ans + 2*(long long)m)%(long long)m);
    return 0;
}