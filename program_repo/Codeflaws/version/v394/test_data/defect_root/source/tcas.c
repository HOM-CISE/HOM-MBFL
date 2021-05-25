#include<stdio.h>
#include<math.h>
int main(int argc, char *argv[])
{
	int a[10],i,j=0,c=0,b[6];
	for(i=0;i<10;i++)
	{
		a[i]=0;
	}
	for(i=0;i<6;i++)
	{
		scanf("%d",&b[i]);
		a[b[i]]++;
	}
	for(i=0;i<10;i++)
	{
		if(a[i]>=4)
		{
			c++;
		}     
		if(a[i]==1)
		{
			j++;
		}
	}
	if(((c==1)&&(j==0))||((c==2)&&(j==0)))
	{
		printf("Elephant\n");
	}
	else if(((c==1)&&(j==1))||((c==1)&&(j==2)))
	{
		printf("Bear\n");
	}
	else
	{
		printf("Alien\n");
	}
	return 0;
}
