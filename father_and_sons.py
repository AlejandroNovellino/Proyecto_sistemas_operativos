#from asyncio.windows_events import NULL
#from email import message
import sys
import os
import signal
import time

def write_to_pipe():
    print("---- Mensaje enviado")
    text = b"SIGALRM recibido"
    os.write(w, text)

def read_from_pipe():
    print("**** Mensaje se esta leyendo")
    pipe_message_r = os.fdopen(r)
    print("**** Mensaje leido: "+pipe_message_r.read())

# defining the signal handler
def pipe_handler(signum, frame):
    # write to the pipe
    write_to_pipe()

# create the pipe for comunication 
# between the two child process
r, w = os.pipe()
pipe1_closed, pipe2_closed = False, False

# create the first child process
pid_1 = os.fork()
# create the second child process
pid_2 = os.fork() if (pid_1 > 0) else None
print(os.getpid())
if(pid_1 == 0):
    print("Hello from the first child, id:"+str(os.getpid()))
    signal.signal(signal.SIGALRM, pipe_handler)
    signal.alarm(1)
    ####
    os.close(r)
    #signal.signal(signal.SIGALRM, pipe_handler)
    signal.alarm(1)

else:
    if(pid_2 == 0):
        print("Hello from the second child, id: "+str(os.getpid()))    
        time.sleep(1.1)
        read_from_pipe()
        ####
        time.sleep(1.1)   
        os.close(w)
        read_from_pipe()

    else: 
        print("Hello from the father, id: "+str(os.getpid()))

time.sleep(4)
sys.exit()
