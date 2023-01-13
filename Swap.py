#1.Swaping two number
#1.1 using a third variable
'''A=100
B=200
print("Before swap A=",A)
print("Before swap B=",B)
C=A
A=B           # >> Logic
B=C
print("After swap A=",A)
print("After swap B=",B)
'''

#1.2 without using a third variable
'''A=100
B=200
print("Before swap A=",A)
print("Before swap B=",B)
A=A+B
B=A-B
A=A-B
print("After swap A=",A)
print("After swap B=",B)'''

#1.3 A,B=B,A >> By assigning multiple Variable in single stateent
A=input("Enter the value of A:")    #takes string as input
B=input("Enter the value of B:")
print("Before swap A=",A)
print("Before swap B=",B)
A,B=B,A
print("After swap A=",A)
print("After swap B=",B)
