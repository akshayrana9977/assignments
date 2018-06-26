def check(fun):
    def checkadd(x,y):
        if x<y:
            fun(x,y)
        else:
            z=x-y
            print("BY CHECKADD Z : ",z)
    return checkadd


@check
def add(a,b):
    z=a+b
    print("ANSWER IS : ",z)
