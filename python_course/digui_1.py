#ditui 1
def rev(s):
    if s == "" :
        return s
    else :
        return rev(s[1:])+s[0]
    
print (rev("abcdef"))
