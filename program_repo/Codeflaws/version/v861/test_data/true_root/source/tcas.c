#include <stdio.h>
int main(int argc, char *argv[])
{
	int n,i,max=0,maxp,min=101,minp;
	int ans1,ans2;
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
		if(max < a[i])
		{
			max = a[i];
			maxp = i;
		}
		else if(min > a[i])
		{
			min = a[i];
			minp = i;
		}
	}
	if(n==1)
	{
		printf("0\n");
		return 0;
	}

	if(n==2)
	{
		printf("1\n");
		return 0;
	}
	if(maxp > (n-1-maxp))
		ans1 = maxp;
	else
		ans1 = (n-1-maxp);
	if(minp > (n-1-minp))
		ans2 = minp;
	else
		ans2 = (n-1-minp);
	if(ans1>ans2)
		printf("%d\n",ans1);
	else
		printf("%d\n",ans2);
  return 0;
}





