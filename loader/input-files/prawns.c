#include<stdio.h>
void main()
{
    int a , x , i , j , b , k , c ;
    extern int i , j , l ,m , n ;
    extern char p , q ;
    printf("\nEnter number of points starting from school:");
    scanf("%d",&b);
    for(i=0;i<b;i++)
    {
        printf("\n*Enter number of ways to reach point %d:",i);
        scanf("%d",&x);
        for(j=0;j<x;j++)
        {
            printf("\nEnter distance of path %d to reach that point :",j);
            scanf("%d",&a[i][j]);
        }
    }
    printf("\nEnter distance of another path from last point to school:");
    scanf("%d",&c);
    for(i=0;i<b;i++)
    {
        k[i]=a[i][0];
        for(j=0;j<x;j++)
        {
            if(k[i]>a[i][j])
            {
                k[i]=a[i][j];
            }
        }
    }
    printf("\nPaths selected are:");
    for(i=0;i<b;i++)
    {
        printf("\t%d",k[i]);
    }
    x=0;
    for(i=0;i<b;i++)
    {
        x=x+k[i];
    }
    if(c<x)
    {
        printf("\nOverall path is circular");
        printf("\nTotal shortest distance = %d",x+c);
    }
    else if(c>x)
    {
        printf("\nPath is retraced");
        printf("\nTotal shortest distance = %d",x+x);
    }
    else if(c==x)
    {
        printf("\nAvailabel paths to go back to school are of eqaul distance");
        printf("\nTotal shortest distance = %d",x+x);
    }
}