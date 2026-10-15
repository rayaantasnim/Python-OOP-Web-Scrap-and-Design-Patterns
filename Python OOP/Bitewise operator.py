#Value Destribute
a = 5        #Binary - 0101
b= 11        #Binary - 1011

#AND operator
print ("AND operator")
print (a&b)

#Logics:
print ("In Binary format:")
print ("0 + 0 = 0")
print ("0 + 1 = 0")
print ("1 + 0 = 0")
print ("1 + 1 = 1")

print ("")
#OR operator
print ("OR operator")
print (a|b)

#Logics: 
print ("In Binary format:")
print ("0 + 0 = 0")
print ("0 + 1 = 1")
print ("1 + 0 = 1")
print ("1 + 1 = 1")

print("")
#XOR operator
print ("XOR operator")
print (a^b)

#Logics:
print ("In Binary format:")
print ("0 + 0 = 0")
print ("0 + 1 = 1")
print ("1 + 0 = 1")
print ("1 + 1 = 0")

print ("")
#NOT operator
print ("NOT operator")
print (~a)
#Short cut: ans of NOT operator = minus (input value + 1)

#Logics:
print ("In Binary format:")
print ("1 = 0")
print ("0 = 1")

#Negative decimal value conversion to binary:
#Determine the binary value of positive decimal
#Apply "One’s Complement", opposite the digits 1 or 0
#Add 1 with the result in Binary format





print ("")
#Right Shift Operator
#Logics:
#Push the 8 bit Binary digits to 1 bit right
print ("Right Shift Operator")


print (a>>1)

#Logicss of a>>1:
#a binary = 00000101
#a right 1 shift operator final result binary = 00000010
# 00000010 binary = decimal 2
# so, a>>1 = 2

print (a>>2)

#Logics of a>>2:
#a binary = 00000101
#a right 1 shift operator result binary = 00000010
#Push the 8 bit Binary digits to 1 bit right [again]
#a right 2 shift operator final result binary = 00000001
#00000001 binary = decimal 1
#so, a>>2 = 1

print("")
#Left Shift Operator
#Logics:
#Push the 8 bit Binary digits to 1 bit left
print ("Left Shift Operator")
print (a<<1)

#Logics:
#a binary = 00000101
#a left 1 shift operator final result binary = 00001010
# 00001010 binary = decimal 10
# so, a>>1 = 10

print (a<<2)
#Logics:
#a binary = 00000101
#a left 1 shift operator result binary = 00001010
#a left 2 shift operator, push 1 unit again
#result = 00010100
#Decimal = 20