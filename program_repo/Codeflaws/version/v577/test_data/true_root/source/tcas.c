//385276194
#include <stdio.h>

int main(int argc, char *argv[]) {
  int a,b,c,d,n;
  int u,w,f1,f2,f3,f4,s,f;
  scanf("%d %d %d %d %d", &n, &a, &b, &c, &d);
  int count=0;
  
  f=1;
  for (f1=1; f1<=n; f1++) {
      s=a+b+f1;
      f2=s-a-c;
      f3=s-b-d;
      f4=s-c-d;
      if (f2>=1 && f2<=n &&
	  f3>=1 && f3<=n &&
	  f4>=1 && f4<=n) count++;
  }
  printf("%d",n*count);
  return 0;
}

/*
f1 a f2
b  w c
f3 d f4


f1 1 f2
2  x  1
f3 3 f4

n=5
*/
