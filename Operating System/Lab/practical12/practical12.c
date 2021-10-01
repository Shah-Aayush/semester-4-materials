// C program for Best Fit Algorithm

#include<stdio.h>
#include<process.h>

void main()
{
    int a[20],p[20],i,j,n,m;
    printf("Enter no of Blocks:\n");
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        printf("Enter the No. %d Block size: ",i);
        scanf("%d",&a[i]);
    }
    printf("\nEnter no of Processes:\n");
    scanf("%d",&m);

    for(i=0;i<m;i++)
    {
        printf("Enter the size of Process no. %d: ",i);
        scanf("%d",&p[i]);
    }

    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(p[j]<=a[i])
            {
                printf("\nThe Process %d allocated to %d",j,a[i]);
                p[j]=10000;
                break;
            }
        }
    }

    for(j=0;j<m;j++)
    {
        if(p[j]!=10000)
        {
            printf("\nThe Process %d is not allocated",j);
        }
    }
}