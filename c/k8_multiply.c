#include <stdio.h>

int multiply(int a, int b);

int main(void)
{
  printf("%i\n", multiply(512,657));
}

int multiply(int a, int b)
{
  int product = a * b;
  return product;
}