#digui3 han nuo ta
count = 0
def hnt(n,src,dst,mid):
    global count
    if n == 1 :
        print("{} : {} --> {}".format(1,src,dst))
        count +=1
    else:
        hnt(n-1,src,mid,dst)
        print("{} : {} --> {}".format(n,src,dst))
        count +=1
        hnt(n-1,mid,dst,src)
        
              
hnt(3,"A","C","B")
