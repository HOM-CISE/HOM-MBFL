#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char *argv[])
{
    long long h1,h2,a,b,h,step,days;

    scanf("%lld %lld",&h1,&h2);
    scanf("%lld %lld",&a,&b);

    if(b>a && (8*a)<(h2-h1))
        printf("-1");

    else if(8*a >= h2-h1)
        printf("0");

    else
    {
        h = h2 - (h1 + 8*a);
        step = 12*(a-b);
        days = ceil((double)h/step);
        printf("%lld",days);
    }

    return 0;
}