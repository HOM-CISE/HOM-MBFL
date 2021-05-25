#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    int i, n;
    char name[101][11], status[101][11];
    scanf("%d", &n);

    for(i=0;i<n;i++)
    {
        scanf("%s %s", name[i], status[i]);
    }
    for(i=0;i<n;i++)
    {
        if(status[i][0]=='r')
            puts(name[i]);
    }
    for(i=0;i<n;i++)
    {
        if(status[i][0]=='w' || (status[i][0]=='c' && status[i][1]=='h'))
            puts(name[i]);
    }
    for(i=0;i<n;i++)
    {
        if(status[i][0]=='m')
            puts(name[i]);
    }
    for(i=0;i<n;i++)
    {
        if(status[i][0]=='c' && status[i][1]=='a')
            puts(name[i]);
    }
    return 0;
}
