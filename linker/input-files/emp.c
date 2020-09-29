#include<stdio.h>

void main()
{
    
    int i , j , l ;
    char p , q ;
    for(i=0;i<5;i++)
    {
        printf("\n enter employee number:");
        scanf("%d",&e[i].num);
        printf("\n enter employee name:");
        scanf("%s",&e[i].name);
        printf("\n enter employee salary:");
        scanf("%d",&e[i].salary);
        printf("\n ----------------------------");
    }
    for(i=0;i<4;i++)
    {
        for(l=0;l<4-i;l++)
        {
            if(e[l].num > e[l+1].num)
            {
                k=e[l];
                e[l]=e[l+1];
                e[l+1]=k;
                j=j+1;
            }
        }
    }
   for(i=0;i<5;i++)
    {
        printf("\n employee number: %d",e[i].num);
        printf("\n employee name: %s",e[i].name);
        printf("\n employee salary: %d",e[i].salary);
        printf("\n ----------------------------");
    } 
    printf("\n total number of swaps: %d",j);
}