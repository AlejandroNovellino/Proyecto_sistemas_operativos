import sys 
import os
import timeit

#Codigo para probar
code_to_run = 'os.system(" ".join(sys.argv[1:]))'
#Numero de veces
number_times = 1
#Calculando el tiempo
time_spent = timeit.timeit(stmt=code_to_run, number=number_times, globals=globals())
#Pmprimiendo respuesta
print(f"\nEl tiempo que tardo el programa {' '.join(sys.argv[1:])} fue: {time_spent} segundos")
