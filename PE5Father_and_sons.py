import multiprocessing
import signal
import threading
import time

# defining the signal handler
def pipe_handler(signum, frame):
    # write to the pipe
    queuePipe.put("SIGALRM recibida")

# global variable for the read process
queuePipe = multiprocessing.Queue()

#### set the alarm
signal.signal(signal.SIGALRM, pipe_handler)

def child1_function(queuePipe):
    # write to the pipe 10 times
    for i in range(10):
        # generate the alarm to write
        signal.alarm(2)
        # wait for the signal to happend
        time.sleep(2)

def child2_function(queuePipe):
    # read from the pipe 10 times
    for j in range(10):
        # wait for the first child to write
        time.sleep(2)
        # print the content in the pipe
        print(queuePipe.get())
        ## end 

def main():
    # child processes
    child1 = threading.Thread(target=child1_function, args=(queuePipe,))
    child2 = threading.Thread(target=child2_function, args=(queuePipe,))

    # start the child processes
    child1.start()
    child2.start()

    # wait for them
    child1.join()
    child2.join()

    # print
    print("Proceso padre finalizado")

main()
