#include<stdio.h>
#include<math.h>

int main(int argc, char *argv[])
{
	long long int k,l,i=1,res=1;

	scanf("%lld%lld",&k,&l);



	while(1)
	{
		res=(float)(pow(k,i));
		i++;

		if(l%res!=0)
		{
			printf("NO");
			goto label;
		}

		if(l%res==0&&l/res==1)
		break;
	}

	printf("YES\n");
	printf("%lld",i-2);

	label:

	return 0;
}
