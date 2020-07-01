// Description:
// In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

// Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C).

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