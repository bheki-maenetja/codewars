#include <stdio.h>

int factorial(int a);

int main(void)
{
  int my_num;
  printf("Enter a number: ");
  scanf("%d", &my_num);
  int my_factorial = factorial(my_num);
  printf("The factorial of %d is %d\n", my_num, my_factorial);
}

int factorial(int n)
{
  if (n < 0 || n > 12)
  {
    return -1;
  }
  else if (n == 0)
  {
    return 1;
  }
  
  if (n == 1)
  {
    return n;
  }
  else
  {
    return n * factorial(n - 1);
  }
}