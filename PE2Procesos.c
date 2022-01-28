#include <stdio.h>
#include <sys/resource.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <sys/types.h>
#include <pwd.h>
#include <sys/stat.h>
#include <fcntl.h>
  
int main() {


//Definicion de las estructuras limite que se envia por parametro a la funcion getrlimit y de la estructura passwd para obterner el nombre del usuario.
  
  struct  rlimit limite;
  struct  passwd *p=getpwuid(getuid());
  
  
    //se invoca a la funcion getrlimit pasandole como atributos el comando RLIMIT_NPROC que segun el manual de linux se utiliza 
    //para obtener el numero maximo de procesos que puede tener activos por cada usuario luego
    // se le pasa una estructura de tipo limite en la cual se insertara el valor limite de procesos.
      getrlimit(RLIMIT_NPROC,&limite);
  printf("%s Este es el numero maximo de procesos:  %ld  \t\n",p->pw_name, limite.rlim_cur);
     
      
    return 0;
}
