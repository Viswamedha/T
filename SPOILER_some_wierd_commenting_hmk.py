import threading, queue, time
def f():
    byn = que.get() 
    creds = ftoc(byn) #creds is somthing to do with math and whatever u got from the 'queue'
    que.task_done() #put task done in the queue?
    print(str(creds)+' C') #print stuff
    return creds
def ftoc(num):
    return a9(a5(a32(num))) #something to do wth lots of calculations idrk

def a9(n): #func to divide some value with 9
    return n/9 

def a5(n): #func to multiply a val with 5
    return n*5

def a32(n): #func to subtract 32 from a acertain val
    return n-32

def main():
    number = int(input("Why was I born: ")) #how would u answer with an int to this question
    global que #make it usable for the whole program
    que = queue.Queue() #something with queue again
    que.put(number) # putting the number in the queue?
    threading.Thread(target=f, daemon=True).start() #does the calculation?


    que.join() #program goes on after calc is done
    time.sleep(1) #waits for 1 sec(no reason)
    print('done thank god relive me of this stress') # dunno y he does this

if __name__ == '__main__':    #?
    main()                    #?

