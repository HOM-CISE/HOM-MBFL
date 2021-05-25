#include<stdio.h>
int main(int argc, char *argv[])
{
    char a[100005];
    long int n,i,j,count=0;
    scanf("%ld",&n);
    for(i=0;i<n;i++)
        scanf("%s",&a[i]);
        if(n>26)
        {
            printf("-1");
            return 0;
        }
    for(i=0;i<n;i++)
    {
        if(a[i]==32)
            continue;
        for(j=i+1;j<n;j++)
        {
            if(a[i]==a[j])
            {
                a[j]=' ';
                count++;
            }
        }
    }
    printf("%ld",count);
    return 0;
}

