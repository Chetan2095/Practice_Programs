#SI-Simple Interest:-

Principle=int(input("Enter Principle Amount P= Rs."))    #inputes from user
Time=int(input("Enter Time T= "))                        #typecast from str to int
Rate=int(input("Enter Rate R="))

SI=(Principle*Time*Rate)/100                              # '/' return float value

print("Simple Interest is =",SI)