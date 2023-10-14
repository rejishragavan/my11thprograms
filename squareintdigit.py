def convert_int_to_square():
    x=int(input("Enter the value"))
    res=0
    while a>0:
        a=x%10
        res=res+(a**2)
        a=int(a/10)
    print("result is",res)