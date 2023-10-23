def dictionaryfunc():
    # dictionalry properties
    # 1. mutable
    # 2. unordered .. so we cannot acces elements using index
    # 3. it does not allow duplicates -> It will over write old values
    # 4. It is heterogeneous collection
    # 5. keys alwasy string

    # Create dict using constructor .. use only singel bracket for dictionary.. using doubel brackets like sets, tuple and lsit will throw error
    # though number, string and tupels can be used for key in costructor number is not allwed in constructor
    d = dict(a="Appu", b="Ragav", c="Rasika")
    print(d)

    # Create dict using brackets
    d = {'a': 'Appu', 'b': 'Ragav', 'c': 'Rasika'}
    print(d)

    # acess elements using for loop -- for loop will return keys only nto the pairs
    d = {'a': 'Appu', 'b': 'Ragav', 'c': 'Rasika'}
    for i in d:
        print(i)

    # access elements using for loop - access key-value pair
    d = {'a': 'Appu', 'b': 'Ragav', 'c': 'Rasika'}
    for i in d.items():  # return key-value pair
        print(i)
        print(type(i))

    # access only keys
    d = {'a': 'Appu', 'b': 'Ragav', 'c': 'Rasika'}
    k = d.keys()
    print(k)
    print(type(k))

    # access only keys
    d = {'a': 'Appu', 'b': 'Ragav', 'c': 'Rasika'}
    v = d.values()
    print(v)

    # acces values using key
    d = {'a': 'Appu', 'b': 'Ragav', 'c': 'Rasika'}
    print(d.get('b'))

    # access values - option 2
    d = {'a': 'Appu', 'b': 'Ragav', 'c': 'Rasika'}
    k = d.keys()
    for i in k:
        print(d.get(i))

    # access values - option 3
    d = {'a': 'Appu', 'b': 'Ragav', 'c': 'Rasika'}
    k = d.keys()
    for i in k:
        print(d[i])

    # update value for an existing key -- option 1
    d = {'a': 'Appu', 'b': 'Ragav', 'c': 'Rasika'}
    print(d)
    d['c'] = "Priya"
    print(d)

    # update value for an existing key -- option 1
    d = {'a': 'Appu', 'b': 'Ragav', 'c': 'Rasika'}
    print(d)
    d.update({'a': "Priya"})
    print(d)

    # add element
    d = {'a': 'Appu', 'b': 'Ragav', 'c': 'Rasika'}
    d.update({'d': "Priya"})  # option 1
    d['e'] = "Rejish"  # option 2
    print(d)

    # remove item clear, pop, popitem
    d = {'a': 'Appu', 'b': 'Ragav', 'c': 'Rasika'}
    print(d)
    v = d.pop('b')  # it returns value
    print(v)
    print(d)
    v = d.popitem()  # popt last item from the dict . it returns key-value pair as dict
    print(d)
    print(v)
    d.clear()
    print(d)

    # copy a dictionary
    d = {'a': 'Appu', 'b': 'Ragav', 'c': 'Rasika'}
    e = d.copy()  # e=d will poitn to same dictionary
    e['b'] = "Priya"
    print(d)
    print(e)

    # Dictionary hetrogeneous
    # only numbers, string, tuple are allowed for keys but value can be any thing
    # list can be value
    # set can be a value
    # tuple can be value
    # dictionay itself can be value
    d = {'a': 'Appu', 'b': 'Ragav', 'c': 'Rasika'}
    d['d'] = [1, 2, 3, 4]
    d['e'] = (12, 13, 14)
    d['f'] = {"m1": 20, "m2": 30, "m3": 40}
    d['g'] = {21, 22, 23, 24}
    print(d)