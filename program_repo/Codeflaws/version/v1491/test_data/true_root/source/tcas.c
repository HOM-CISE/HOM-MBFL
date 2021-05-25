#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int n, a, b;
    scanf("%d %d %d", &n, &a, &b);
    printf("%d\n", (a+1 < n-b)?(n-b):(n-a));
    return 0;
}
