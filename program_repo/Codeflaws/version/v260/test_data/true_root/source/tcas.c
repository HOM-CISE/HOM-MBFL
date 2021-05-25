#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{int m,x,y;
    scanf("%d %d %d",&m,&x,&y);
    if (((y>(m-2)/2)&&(y<(m+2)/2)&&(x>(m-2)/2)&&(x<(m+2)/2))||(m==2)) {printf("NO");}
    else printf("YES");

    return 0;
}
