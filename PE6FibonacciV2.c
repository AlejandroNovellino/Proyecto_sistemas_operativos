



#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>
#include <math.h>

int a = 0;
long long int total = 0;

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

void *fibo (void* argA) //Este metodo se encarga de mandarle la funcion fibonacci a los 32 diferentes threads
{
	for (register int i=0; i< 31250; i++) //Se divide en 32 threads para realizar las 31250 repeteciones con los 19 numeros aleatorios
	{
			a=fib(rand()%19);
			total=total + a;	//Variable global total
	}
}

int main()
{
	pthread_t tid;
 	for (register int i = 0; i < 32; i++) //Este for se encarga de generar los 32 threads
	    pthread_create(&tid, NULL, fibo, (void *)&tid);
	pthread_join(tid, NULL); //Se encarga de unir los threads para la suma total
	printf("Suma total de la sucesion de fibonacci: %lld \r\n", total);
}
