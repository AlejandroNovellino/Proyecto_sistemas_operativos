import os
import sys

# program arguments: buffer_size from_file destiny  _file

# get the buffer size
try:
    buffer_size = int(sys.argv[1])
    # verify the buffer size is valid
    if(buffer_size<1 or buffer_size>16384):
        print("Tamaño de buffer no es valido, debe pertenecer al intervalo [1, 16384]")
        exit()
except:
    print("No se introdujo un tamaño de buffer")
    exit()
# get the file to copy
try:
    from_file_name = sys.argv[2]
except:
    print("No se introdujo un archivo a copiar")
    exit()
# get the file to put the data in
try:
    to_file_name = sys.argv[3]
except:
    print("No se introdujo un archivo a crear")
    exit()
# the copy operation
try:
    # open the file to read
    with os.fdopen(os.open(from_file_name, os.O_RDONLY), mode='r', buffering=buffer_size) as from_file:
        try:
            # create or open the file to save the data
            with os.fdopen(os.open(to_file_name, os.O_RDWR | os.O_CREAT), mode='w', buffering=buffer_size) as to_file:
                while True:
                    data = from_file.read(buffer_size)
                    if not data:
                        break
                    to_file.write(data)
        except:
            print("No se pudo crear el archivo destino")
except:
    print("No existe el archivo fuente")
