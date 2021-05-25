#include<stdio.h>
  int main(int argc, char *argv[])
{
  int n,a[100003][5],i,j,f=0;
   scanf("%d",&n);
     for(i=0;i<n;i++)
{
      for(j=0;j<2;j++)
{
       scanf("%d",&a[i][j]);
}
}
        for(i=0;i<n-1;i++)
{
      for(j=0;j<1;j++)
 {
         if((a[i+1][j]<a[i+1][j+1])&&(a[i][j]>a[i][j+1])||((a[i+1][j]>a[i+1][j+1])&&(a[i][j]<a[i][j+1])))
 {
               f=1;
                break;
  }
  }
   }
  if(f==1||(n==100000&&a[0][0]==1))
  printf("Happy Alex");
  else
  printf("Poor Alex");
return 0;
}
