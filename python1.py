#Set(A)
def count_down(n):
    output=[]
    for i in range (n,-1,-1):
        output.append(i)
    return output
print(count_down(5))





def print_and_return(num):
    print(num[0])
    return num[len(num)-1]

print_and_return([1, 2])
print(print_and_return([1, 2]))  







def first_plus_length(lst):
    return lst[0] + len(lst)

first_plus_length([1, 2, 3, 4, 5])
print(first_plus_length([1, 2, 3, 4, 5]))  






def values_greater_than_second(lst):

    result = [x for x in lst if x > lst[1]]
    
    print(len(result))  
    return result    
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))  



def length_and_value(len, value):
    return [value] * len


print(length_and_value(4, 7))  

#Set (B)
# 1
def Biggie_Size(num):
        if num > 0:
             return "Big"
        else:                              
             return num            
print(Biggie_Size(10))
print(Biggie_Size(-50))

#2
def count_positive(num):
    total=0 
    for i in range(len (num)) :
        if num [i] > 0: 
            total+=num[i]
    num[len (num) -1]=total 
    return num
print(count_positive([0,1,2,3,4,5,6, 7,8]))



#3
def sum_total(num):
    sum=0
    for i in range(len(num)):
          sum+=i                    
    return sum

print(sum_total([0,1,2,3,4,5,6,7,8]))
#4
def Average(num):
    sum=0
    for i in range(len(num)):
        sum+=i                        
    Average = sum /len(num)
    return Average
print(Average([0,1,2,3,4,5,6,7,8]))
#5
def minimum(num):
    if num==[]:
         return False
    else:
         return min(num)                
print(minimum([7,49,5,37,29,9]))
print(minimum([]))



#set 3
#1
def greet(name="Guest", time_of_day="day"):
    print(f"Good {time_of_day}, {name}")

greet(time_of_day="morning", name="Nesma")

#2
def Grade_Check(score):
    return "pass" if score>=60  else  "Fail"   

print(Grade_Check(85))

#3
fruits = ["apple", "banana", "cherry"]

fruits[0], fruits[2] = fruits[2], fruits[0]
print(fruits)
#4
Text="coding is fun"
print(Text[10:])               
print(Text[::-1])
print(Text[:6])

#5

data = [42, 10, 77, 2, 15]

largest = max(data)
total = sum(data)
sort = sorted(data)

print("Largest number:", largest)
print("Total sum:", total)
print("Sorted list:", sort)
