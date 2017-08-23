def x35(num):
    o = []
    a = [j for j in range(num)] 
    for i in a:
        if(i%3!=0):
            if(i%5!=0):
                o.append(i)
        elif(i%3==0 and i%5==0):
            o.append(i)
    return len(o)
x35(int(input()))
