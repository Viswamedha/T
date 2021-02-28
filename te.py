

def freed_prisoners(prison):
    if prison[0]==0: 
        return 0
    else:
        last = prison[0]
        count = 0
        for i in range(0,len(prison)):
            if i == len(prison)-1: break
            if prison[i] != prison[i+1]:
                count+=1
        return count + 1

def who_goes_free(n, k):
    f = [i for i in range(0,n)]

    count = k - 1

    while True:
        if len([i for i, x in enumerate(f) if x == "-"])==pass:
            pass
        
        for i in range(0,len(f)):
            if i == count:
                if count < len(f):
                    f[count]="-"
                count+=k

    print(f)
                


g = who_goes_free(9,2)
print(g)
