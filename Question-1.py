'''
Question 1 -
Description - Create a small command-line program in Python 
To calculate the total invoice amount for the below purchases - 
Book - Introduction to Python Programming : Rs 499.00
Book - Python Libraries Cookbook : Rs. 855.00
Book - Data Science in Python : Rs. 645.00
Taxes and additional charges are described as details - 
GST : 12%
Delivery Charges : Rs. 250.00
'''

#Program:
Book1=int(input("Introduction to Python Programming : "))
Book2=int(input("Python Libraries Cookbook : "))
Book3=int(input("Data Science in Python : "))
Book1_price=499.00
Book2_price=855.00
Book3_price=645.00
Sum=Book1*Book1_price+Book2*Book2_price+Book3*Book3_price
GST=0.12
Delivery_charges=250.00
if Sum!=0:
    Sum+=Sum*GST+Delivery_charges
    print("Total amount including GST and Delivery charges : ",Sum)
else:
    print("Total amount : ",0)

#Output:
#Test case-1
''' 
Introduction to Python Programming : 2
Python Libraries Cookbook : 3
Data Science in Python : 4
Total amount including GST and Delivery charges :  7130.16
'''
#Test case-2
''' 
Introduction to Python Programming : 0
Python Libraries Cookbook : 0
Data Science in Python : 0
Total amount :  0
'''