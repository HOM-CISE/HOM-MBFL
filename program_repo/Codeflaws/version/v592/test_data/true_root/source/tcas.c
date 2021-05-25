#include<stdio.h>
int main(int argc, char *argv[])
{
    int i,j,k,b=0,w=0;
    char a;
    for(i=0;i<8;i++)
    {
        for(j=0;j<8;j++)
        {
            scanf("%c",&a);
            if(a=='Q') w=w+9;
            if(a=='R') w=w+5;
            if(a=='B') w=w+3;
            if(a=='N') w=w+3;
            if(a=='P') w=w+1;
            if(a=='q') b=b+9;
            if(a=='r') b=b+5;
            if(a=='b') b=b+3;
            if(a=='n') b=b+3;
            if(a=='p') b=b+1;


        }

    }
    if(w>b)
    printf("White");
    else if (w<b) printf("Black");
    else if (w==b) printf("Draw");
return 0;
}
