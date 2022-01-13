import sys


# get the buffer size
try:
    buffer_size = int(sys.argv[1])
    # verify the buffer size is valid
    if(buffer_size<1 or buffer_size>16384):
        print("Tamano de buffer no es valido, debe pertenecer al intervalo [1, 16384]")
        exit()
except:
    print("No se introdujo un tamano de buffer")
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
# open the file
try:
    with open(from_file_name, buffering=buffer_size) as file:
        info_to_save = file.read()
        try:
            with  open(to_file_name, "w", buffering=buffer_size) as new_file:
                new_file.write(info_to_save)
            print("El archivo se ha copiado exitosamente")
        except:
            print("No se pudo crear el nuevo un archivo")
            exit()
except:
    print("No existe el archivo")
