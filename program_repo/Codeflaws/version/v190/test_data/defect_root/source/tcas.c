#include<stdio.h>
#include<string.h>
int main(int argc, char *argv[])
{
    long long  int a,c,b,sum,check=0,itr=300,x,y=0;
    scanf("%lld %lld %lld",&a,&b,&c);
    while(itr--)
    {
        x=(c-(b*y))/a;
        if((a*x+b*y)==c&& x>=0&&y>=0)
        {
            check=1;
            //printf("%lld %lld",x,y);
            printf("Yes\n");
            break;
        }
        y++;
    }
    if(check==0)
    {
        printf("No\n");
    }
    return 0;
}
