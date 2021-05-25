#include<stdio.h>
typedef  long long int LL;
LL mod=1000000009;
LL qk(LL a,LL b)
{
    LL anss=1;
    while(b)
    {
        if(b%2==1)
            anss=anss*a%mod;
        a=a*a%mod;
        b=b/2;
    }
    return anss;
}

int main(int argc, char *argv[])
{
    LL n,m,k,wr,t,ans,l;
    scanf("%lld %lld %lld",&n,&m,&k);
    wr=n-m;
    t=n/k;
    if(wr>=t) printf("%lld\n",m);
    else 
    {
        l=t-wr;
        ans=qk(2,l+1)-2;
        ans=(ans*k+n%k+wr*k-wr)%mod;
        printf("%lld\n",ans);
    }
    return 0;
}


   	      	   		 		      	   	