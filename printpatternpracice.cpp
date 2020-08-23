/* *      *      
    *   *
      *
    *   *
   *      * 
#include<stdio.h>
int main()
{
	int i,j,n=5;
	for(j=1;j<=n;j++)
	{
		for(i=1;i<=n;i++)
		{
			if(i==j)
			printf("*");
			else if((i+j)==n+1)
			printf("*");
			else
			printf(" ");
		
		}
		printf("\n");
	}
}


1
2 4
1 3 5
2 4 6 8
1 3 5 7 9

#include<stdio.h>
int main()
{
	int i,j,n=5;
	for(j=1;j<=n;j++)
	{
		for(i=1;i<=j;i++)									
		{
			if(j%2==0)
			printf("%d ",2*i);		
			else if (j%2!=0)
			printf("%d ",2*i-1);
			else
			printf(" ");
		}
		printf("\n");
	}
}
1
2*3
4*5*6
4*5*6
2*3
1

#include<stdio.h>
int main()
{
	int i,j,t=1,k=4;
	for(j=1;j<=3;j++)
	{
		for(i=1;i<=j;i++)
		{
			if(i!=j)
			{
				printf("%d*",t);
				t++;
			}
			else{
				printf("%d",t);
				t++;
			}
		}
		printf("\n");
	}
	for(i=3;i>=1;i--)
	{
		for(j=1;j<=i;j++)
		{
			if(j!=i)
			{
				printf("%d*",k);
				k++;	
			}
			else
			{
				printf("%d",k);
				k++;
			}
		}printf("\n");
		k=i-1;
	}
}
