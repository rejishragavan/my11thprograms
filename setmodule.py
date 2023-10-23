def setfunction():
    # set properties
    # 1. Set is immutable but you can add/remove lements from the set
    # 2. set is unordered .. we cannot access elemetns using index valuve
    # 3. Set does not allow duplicates
    # 4 . Set is heterogenous collection of elements

    # set creation using contructor
    s = set((1, 2, 3, 4, 5))
    print(type(s))
    print(s)

    # set creation using symbols
    s = {1, 2, 3, 4, 5}
    print(type(s))
    print(s)

    # access elements using for loop
    for i in s:
        print(i)  # print each element in the set

    # accessing elements using index
    # we cannot access element using index

    # add elemt to set
    s = {1, 2, 3, 4, 5}
    s.add(6)
    print(s)

    # add one set into another set
    s = {1, 2, 3, 4, 5}
    p = {11, 12, 13, 14, 15}
    s.update(p)
    print(s)

    # add any iterable data structure to set
    s = {1, 2, 3, 4, 5}
    l = [11, 12, 13, 14]
    s.update(l)
    print(s)

    # remove element from set (option 1)
    s = {1, 2, 3, 4, 5}
    a = s.remove(3)  # remove will not return removed element
    print(s)
    print(a)

    # remove element from set (option 2)
    s = {1, 2, 3, 4, 5}
    s.discard(3)  # discard will not return the removed element
    print(s)

    # remove element from set (option 3)
    s = {1, 2, 3, 4, 5}
    a = s.pop()
    print(s)
    print(a)

    # clear removes all elements from the set (option 4)
    s = {1, 2, 3, 4, 5}
    s.clear()
    print(s)

    # set operations --> this will return new set
    # 1. A U B ==> a.union(b)
    # 2. A ^ B ==> a.intersection(b)
    # 3. A - B ==> a.difference(b)
    # 4. B - A ==> b.difference(a)
    # 5. A U B - A ^ B ==> a.symmetric_difference(b)

    # print all elements
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    print(a.union(b))  # c=a.union(b)

    # print common elements
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    print(a.intersection(b))

    # print A - B
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    print(a.difference(b))

    # print  A U B - A ^ B
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    print(a.symmetric_difference(b))

    # create new copy of set
    a = {1, 2, 3, 4, 5}
    b = a.copy()  # b=a
    print(a)
    print(b)