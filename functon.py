def ds(a=1,b="default"):
    print(" 1)List \n 2)Tuple\n 3)Set\n 4)Dictionary")
    i=int(input("Enter type 0f datastructure: "))
    if i==1:         
        l = []
        l.append(a)
        l.append(b)
        print("List:", l)
        a1 = input("Enter new Roll No: ")
        b2 = input("Enter new Name: ")
        l[0] = a1
        l[1] = b2
        print("List:", l)
        del l
        print(l)
    elif i==2:
        t = (a,b)
        print("Tuple:", t)
        a1 = input("Enter new Roll No: ")
        b2 = input("Enter new Name: ")
        t = (a1, b2)
        print("Tuple:", t)
        del t
        print(t)
    elif i==3:
        s = set()
        s.add(a)
        s.add(b)
        print("Set:", s)
        a1 = input("Enter new Roll No: ")
        b2 = input("Enter new Name: ")
        s.remove(a)
        s.add(a1)
        s.remove(b)
        s.add(b2)
        print("Set:", s)
        del s
        print(s)
    elif i==4:
        d = {}
        d['Roll No'] = a
        d['Name'] = b
        print("Dictionry:", d)
        a1 = input("Enter new Roll No: ")
        b2 = input("Enter new Name: ")
        d['Roll No'] = a1
        d['Name'] = b2
        print("Dictionary", d)
        del d
        print(d)
    else:
        print("choose correct option !!")        
ds(102,"shubham")    