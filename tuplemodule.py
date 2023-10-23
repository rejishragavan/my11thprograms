def tuplefunc():
    #tuples properties
    #1. immutable.. we cannot add or remove or update element in tuple
    #2. ordered .. we can access element using index value
    #3. Hetrogeneous
    #4. allow duplicate

    #create tuple using constructor
    tup=tuple((2,))
    print(type(tup))
    print(tup)

    #create tuple using ()
    tup=(5,6,7)
    print(type(tup))
    print(tup)

    #create tupel with one element
    tup=(4,)
    print(type(tup))
    print(tup)

    #tuple allows duplicate
    tup=(4,4,5,5,6,6)
    print(tup)

    #access tuple element - method 1
    tup=(1,2,3,4,5)
    for i in tup:
      print(i)

    #access tuple element - method 2 using index
    tup=(11,12,13,14,15)
    for i in range(len(tup)): #by default range will take 0 as initial value
      print(tup[i])

    #get the index position of the given element
    tup=(11,12,13,14,15)
    print(tup.index(13))

    #count the occurance of given element
    tup=(4,4,5,5,6,6)
    print(tup.count(5))

    #how to add/update/remove an element to tuple
    tup=(1,2,3,4,5,6)
    lst=list(tup)
    lst.append(7)
    tup=tuple(lst)
    print(tup)

    #multiply tuple
    tup=(1,2,3,4,5,6)
    tup1=tup*2
    print(tup1)

    #adding/join tuples
    tup1=(1,2,3,4,5,6)
    tup2=(11,12,13,14,15,16)
    tup3=tup1+tup2
    print(tup3)