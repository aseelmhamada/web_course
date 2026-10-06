def countdown(i):

    list=[]
    for x in range(i,-1,-1):              
        list.append(x)
    print (list)
    
    
    
def print_and_return(i):    
    print(i[0])
    
    return(i[len(i)-1])                    #Task 2

print(print_and_return([1,2]))
  
  
  