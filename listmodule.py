def listfunc():
    # list is a collection of heterogeneous data types
    lst = [1, 2, 3, "ragav", [11, 12, 13, 14], (111, 112, 113), {121, 122, 123}, {"m1": 50, "m2": 60, "m3": 70}, 5.5]
    print(lst)

    # list allows duplicate values .. in below list 3 & 4 are duplicate values
    lst1 = [1, 2, 3, 3, 4, 4]
    print(lst1)

    # list is mutable -- below code changes value of 0th element
    lst1 = [1, 2, 3, 3, 4, 4]
    lst1[0] = -1
    print(lst1)

    # list ordered -- list maintain the order in which element is pushed
    lst1 = [1, 2, 5, 4, 3]
    print(lst1)

    # print the type
    lst1 = [1, 2, 3, 3, 4, 4]
    print(type(lst1))

    # access list element -- access list elemnt using subscript/index value
    lst1 = [1, 2, 3, 3, 4, 4]
    print(lst[4])

    # traverse full list
    lst1 = [1, 2, 3, 3, 4, 4]
    for x in lst:
        print(x)

    # access range of list elements -- therre are two syntax to access sub array
    # 1. [start_index:end_index] -- end index excluded
    # 2. [start_index:end_index:increment] -- by default increemnt is 1
    # 3. if start_index=-1 element is accessed from end lst[-1] -> access last element
    # 4. If start index is not mentioned by default it will start from 0the index
    # 5. If end index is not given by default it will go till last element
    lst2 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(lst2[0:5])  # ==> print(lst2[:5])
    print(lst2[2:6])
    print(lst2[:5])
    print(lst2[3:])  # ==> print(lst2[3:8])

    print(type(lst2[3]))  # ==> int
    print(type(lst2[3:7]))  # ==> list

    # acess list element from start index to specified index
    print(lst2[0:5])
    print(lst2[:5])

    # access list element from end index to middle of list
    print(lst2[-1:4:-1])

    # access lsit alternate list element from start of the list
    print(lst2[0::2])

    # access lsit element from end of the list
    print(lst2[-1:-9:-1])

    # Copy the list element
    lst2 = [1, 2, 3, 4, 5, 6, 7, 8]
    lst3 = lst2  # shallow copy
    lst2[1] = -1
    print(lst2)
    print(lst3)

    lst2 = [1, 2, 3, 4, 5, 6, 7, 8]
    lst3 = lst2.copy()  # deep copy
    lst2[1] = -1
    print(lst2)
    print(lst3)

    # Add new element in last of the list
    lst2 = [1, 2, 3, 4, 5, 6, 7, 8]
    lst2.append(9)
    print(lst2)

    # Join two list
    lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
    lst2 = [11, 12, 13, 14, 15, 16, 17, 18]
    lst2.extend(lst1)
    print(lst2)

    # Multiply list
    lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
    lst2 = lst1 * 2
    print(lst2)

    # remove element from list
    lst1 = [1, 2, 2, 3, 4, 5, 6, 7, 8]
    x = lst1.remove(2)  # ==> search by value and remove the first occurance and will nto return the element
    print(x)
    print(lst1)

    print("pop")
    # pop removes the lement in last and return the removed element
    lst1 = [1, 2, 2, 3, 4, 5, 6, 7, 8]
    x = lst1.pop()
    print(x)
    print(lst1)

    # sort list
    lst1 = [1, 4, 7, 3, 2, 6, 5]  # un sroted order lsit
    lst1.sort()  # by default it will sort in ascending order
    print(lst1)

    lst1 = [1, 4, 7, 3, 2, 6, 5]  # un sroted order lsit
    lst1.sort(reverse=True)  # descending order sort
    print(lst1)

    # reverse the list
    lst1 = [1, 4, 7, 3, 2, 6, 5]  # un sroted order lsit
    lst1.reverse()
    print(lst1)

    # find position fo the given element
    lst1 = [1, 4, 7, 3, 2, 6, 5]
    print(lst1.index(3))

    # count the number of occurance for given element
    lst1 = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
    print(lst1.count(5))

    # clear elements from the list
    lst1 = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
    print(lst1)
    lst1.clear()
    print(lst1)

    # count the number of elements in the list
    lst1 = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
    len(lst1)

    # appending a tuple to list
    lst1 = [1, 4, 7, 3, 2, 6, 5]
    tup1 = (12, 13, 14, 15)
    set1 = {111, 112, 113, 114}
    lst1.extend(tup1)
    lst1.extend(set1)
    print(lst1)

    # add element in middle fo the list/at specified position
    lst1 = [1, 4, 7, 3, 2, 6, 5]
    lst1.insert(2, 9)  # ==> inserting 9 in the list before the postion 2
    print(lst1)
