#include<stdio.h>
int main(int argc, char *argv[])
{
    int n,sum,i;
    scanf("%d",&n);
    sum=1;
    for(i=1;i<=n-1;i++)
    {
        sum=sum+i;
        if(sum>n) sum=sum%n;
        printf("%d ",sum);

    }


    return 0;
}
