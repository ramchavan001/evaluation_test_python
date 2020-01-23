#WAPP using function for right rotation:


def right_rotation():
    A=list()
    ni=int(input("Enter the size of the List: "))
    print("Enter the number: ")
    for i in range(int(ni)):
        p=int(input("ni="))
        A.append(int(p))
        print (A)
    r =int(input("enter the right Rotation: "))
    A = (A[-r:] + A[:-r])
    print("After Rotation: ",A)
    
right_rotation()    

    