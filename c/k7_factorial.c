#include <stdio.h>

int factorial(int a);

int main(void)
{
  int my_num;
  printf("Enter a number: \n");
  scanf("%d", &my_num);
  int my_factorial = factorial(my_num);
  printf("The factorial of %d is %d", my_num, my_factorial);
}

int factorial(int n)
{
  return n;
}