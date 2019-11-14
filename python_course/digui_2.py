#digui2
def fb(n):
    if n==1 :
        return 1
    elif n==2 :
        return 1
    else :
        return fb(n-1)+fb(n-2)

print(fb(10))
