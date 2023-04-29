'''
Question 2 - 
Description: Write a program in Python to print the number of unique letters in a string-
Only new letters from the string should be counted and not duplicates.
Input : string1 = "India"
Output : uniqueLetters = i,n,d,a

Input : string1 = "Dedication"
Output : uniqueLetters = d,e,i,c,a,t,o,n
'''

#Program:
My_string=input("string1 = ")
Lower_case=My_string.lower()
list1=[]
UniqueWord=""
for i in range(len(Lower_case)):
    if Lower_case[i] not in list1: 
        list1.append(Lower_case[i])
for j in range(len(list1)):
    UniqueWord+=list1[j]+","
print("UniqueLetters =", UniqueWord[:-1])

#Output:
#Test case-1
''' 
string1 = Suresh
UniqueLetters = s,u,r,e,h
​'''
#Test case-2
'''
string1 = India
UniqueLetters = i,n,d,a
'''
