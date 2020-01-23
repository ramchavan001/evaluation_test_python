#Create a function to search an element x in the user i/p list and return its location(index) if found otherwise return -1
#O/P should be like:
#Enter data: 3 5 2 8 7 6 1
#Element to be searched: 8
#Element is present at location 3

def search_element():
    list=[]
    n=int(input("enter the number of Element for insertion in list: "))
    for i in range(0,n):
        ele=int(input("enter the Element: "))
        list.append(ele)
    
    length=len(list)
    
    a=int(input("enter element for searching: "))
   
    
    for i in range(0,length):
        if a==list[i]:
            print("found")
            break
        if(i+1==length):
            print("not found")
        
    #print("found at index: ",list.index(a))
        
search_element()
        