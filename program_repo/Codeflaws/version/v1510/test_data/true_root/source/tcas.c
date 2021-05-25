#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[])
{
	long long q, p, i, j;
	scanf("%lld", &q);
	for (i = 2LL; i <= sqrt(q); ++i)
		if (q % i == 0LL)
		{
			p = q / i;
			for (j = 2LL; j * j <= sqrt(p); ++j)
				if (p % j == 0LL)
				{
					printf("1\n%lld\n", i * j);
					return 0;
				}
			puts("2");
			return 0;
		}
	puts("1\n0");
	return 0;
}
