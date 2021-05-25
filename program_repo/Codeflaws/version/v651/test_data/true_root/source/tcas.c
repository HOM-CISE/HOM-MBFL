#include <stdio.h>
#include <stdlib.h>

#define MAX_N (200000)

int ws[MAX_N];
int hs[MAX_N];

int main(int argc, char *argv[]) {
  int i,n,h,acc,mx1,mx2;

  scanf("%d", &n);
  for ( i=acc=mx1=mx2=0; i < n; ++i ) {
    scanf("%d %d", ws+i, hs+i);
    acc += ws[i];
    if ( hs[i] > mx1 ) mx1 = hs[i];
    else if ( hs[i] > mx2 ) mx2 = hs[i];
  }
  for ( i=0; i < n; ++i ) {
    h = hs[i] == mx1 ? mx2 : mx1;
    printf("%d ", h*(acc-ws[i]));
  }
  printf("\n");
  return EXIT_SUCCESS;
}
