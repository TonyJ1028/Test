//time difference calculator
#include<stdio.h>
int main()
{
    int h1,m1;//insert first time
    printf("Please insert the first time(HH MM):\n");
    scanf("%d %d",&h1,&m1);
    
    if (h1> 23 || m1 >59)
    {
        printf("Insert error!\n");
        return 0;
    }
    int h2,m2;//insert second time
    printf("Please insert the second time:\n");
    scanf("%d %d",&h2,&m2);
    
    if (h2 > 23 || m2 > 59)
    {
        printf("Insert error!\n");
        return 0;
    }

    int m = h1 * 60 + m1;
    int mc = h2 * 60 +m2;
    int r = m - mc;
    if (r < 0)
        r = -r;
    int hr = (r / 60);int mr = r % 60;

    printf("The time difference is %02d:%02d\n",hr,mr);
    return 0;
}