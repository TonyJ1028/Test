#include<stdio.h>
int main()
{
    int a,b,sum,dif,pro;//define three variables

    printf("please insert the first number:");
    scanf("%d",&a);//must add an "&"before the variables being scanned 
    printf("please insert the second number:");
    scanf("%d",&b);

    sum = a + b;//calculate the summary
    printf("The summary is:%d\n",sum);

    dif = a - b;//calculate the difference
    printf("The difference is:%d\n",dif);

    pro = a * b;//calculate the product
    printf("The product is:%d\n",pro);

    printf("The quotient is:%f\n",(double)a/b);
    return 0;
}