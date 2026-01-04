#List in python
my_list=["apple",'banana',"cherry","date"]
print(my_list)
print(type(my_list))
print(len(my_list))
print(my_list[0])
my_list.append("banana")
print(my_list)
my_list.remove(1)
print(my_list)
my_list.insert(1,"orange")
print(my_list)

#pop() and sort()
my_list=["apple",'banana',"cherry","date"]
my_list.pop()
print(my_list)
my_list.sort() #will give error because list contains different data types
print(my_list)



#Tuple in python
my_tuple=("apple",1,2.4,True)
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))
print(my_tuple[0])#my_tuple[1]="banana" #will give error because tuple is immutable
print(my_tuple)






#Dictionary in python
my_dict={"name":"John","age":30,"is_student":True}
print(my_dict)
print(type(my_dict))
print(len(my_dict))
print(my_dict["name"])
my_dict["age"]=31
print(my_dict)
my_dict["city"]="New York"
print(my_dict)
my_dict.pop("is_student")
print(my_dict)





#Set in python
my_set={"apple",1,2.4,True}
print(my_set)
print(type(my_set))
print(len(my_set))
my_set.add("banana")
print(my_set)
my_set.remove(1)
print(my_set)
my_set.add(2)
print(my_set) #sets do not allow duplicate values
my_set.clear()
print(my_set)


#mini task Question:
'''Write a program that:
Stores 5 student marks in a list
Finds total & average
Stores result in dictionary:
name
total
average
result (Pass / Fail)'''



list=[70,30,80,90,50]

total=sum(list)
average=total/len(list)


if average >= 35:
    result = "Pass"
else:
    result = "Fail"
student={
    "name":"megha",
    "total":total,
    "average":average,
    "result":result
}
print(student)


