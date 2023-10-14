def convert_string():
    x=str(input("Enter the value"))
    print("output value",x)
    result=0
    for c in x:
        y=int(c)
        z=y*y
    #    print("y=",y,"z=",z)
        result+=z
    print("result = ",result)