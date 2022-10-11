def print_rangoli(count):
    string ='abcdefghijklmnopqrstuvwxyz'
    mlen = ((count*2)-1)+((count*2)-2)
    #print(string[count-1])
    str1=str()
    l=[]
    for i in range(count-1,-1,-1):
    #print(i)
        if(i == count-1):
            str1 = '-'.join((string[count-1])).center(mlen,'-')
            l.append(str1)
        else:
            str1 = '-'.join(string[count-1:i:-1] + string[i:count]).center(mlen,'-')
            l.append(str1)

    llen = len(l)
    for i in l:
        print(i)
    for i in range(llen-2,-1,-1):
        print(l[i])