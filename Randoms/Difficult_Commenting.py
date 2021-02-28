import threading, queue, time #import mdoules, the only one I know is time 
def f():    
    byn = que.get()  #Creating variables
    creds = ftoc(byn) 
    que.task_done() 
    print(str(creds)+' CCCCCCCCCC') #print some currency with a symbol
    
    return creds
def ftoc(num):
    return a9(a5(a32(num)))  #Definite confusion

def a9(n): #More confusion
    return n/9 

def a5(n): #More confusion and a twinge of pain
    return n*5

def a32(n): #Pure pain
    return n-32

def main():
    number = int(input("Why was I born: ")) #input
    global que #Global variable so can be used anywhere
    que = queue.Queue() 
    que.put(number) 
    threading.Thread(target=f, daemon=True).start() 


    que.join() 
    time.sleep(1)
    print('done thank god relive me of this stress') 
if __name__ == '__main__':
    main() 
