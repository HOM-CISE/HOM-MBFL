#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]) 
{
    int count[256]={0};
    int countP,i,j;
    char str[1000];
    
    scanf("%s", str);
    
    countP=0;
    for(i=0; i<strlen(str); i++)
    count[str[i]]+=1;
    
    for(i=0; i<256; i++)
    {
        if(count[i]%2==1)
        countP++;
    }
    
    if(countP%2==1 || countP==0)
    printf("First");
    
    else
    printf("Second");
    

    return 0;
}
