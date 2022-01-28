#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>
#include <math.h>

int fib(int n) //Metodo utilizado para calcular la sucesion de Fibonacci
{
    int a = 0, b = 1, c, i;
    if( n == 0)
        return a;
    for(i = 2; i <= n; i++)
    {
       c = a + b;
       a = b;
       b = c;
    }
    return b;
}

int main()
{
	int a; 
	a=0;
	long long int total = 0;
	for (register int i=0; i< 1000000; i++)
	{
			a=fib(rand()%19); //Calcula un fibonacci por cada iteracion y luego suma el total
			total=total + a;	
	}
	printf("Suma total de numeros fibonacci: %lld \r\n", total);
}