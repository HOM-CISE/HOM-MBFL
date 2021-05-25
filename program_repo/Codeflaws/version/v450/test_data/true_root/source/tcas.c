#include<stdio.h>
int main(int argc, char *argv[]){
    int a,b,c=0,d=0,i,j,k,l,z,n,m,x,y;
    scanf("%d%d%d%d%d",&z,&n,&m,&x,&y);
    a=n+m+x+y+z;

 c=a%5;
 if(a==0)
    printf("%d",0);
 else{
 if(c==0){
    printf("%d",a/5);

 }

    else {
        printf("%d",-1);
    }

    }

    printf("\n");
    return 0;
}
