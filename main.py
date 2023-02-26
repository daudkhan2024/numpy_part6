# Arithemetic Operation
import numpy as np


#Addition
var = np.array([1,2,3,4])
varadd = var  +  3
print( varadd)

#Addding two array
var1 = np.array([1,2,3,4])
var2 = np.array([1,2,3,4 ])
varadd = var1 + var2
print(varadd)


# another way
var1 = np.array([1,2,3,4])
var2 = np.array([1,2,3,4 ])
varadd = np.add(var1,var2)
print(varadd)

# Modulus
var = np.array([1,2,3,4])
varadd = var % 3
print(varadd)



a = np.array([1,2])
b = np.array([3,4])
print("subtraction : ",np.subtract(a,b))

print("modolus :  ",np.mod(a,b)) #mode
print("division : ",np.divide(a,b))#divide
print("reciprocal  1/b : ",np.reciprocal(b))#1/b

#2D array
var21 = np.array([[1,2,3,4],[1,2,3,4]])
var22 = np.array([[1,2,3,4],[1,2,3,4]])
print(var21)
print(var22)

varadd2 = var21 + var22
print(varadd2)





varr = np.array([1,2,3,4,53,3,5])
print("min : ",np.min(varr))
print("max : ",np.max(varr))
print("sin : ",np.sin(varr))
print("argmin : ",np.argmin(varr))# to check position of minimum
print("argmax : ",np.argmax(varr))
print("squareroot :",np.sqrt(varr))
var11 = np.array([[2,3,4],[9,7,6]])
print(np.min(var11,axis = 0))#axis 0 is column axis 1 is row


#Broadcasting Numpy Arrays
# must have same dimension
var1 = np.array([1,2,3])
print(var1.shape)
print()
var2  = np.array([[[1],[2],[3]]])
print(var2)
print()
print(var2.shape)

print()
print(var1 + var2)


print()
print()
########### 2*1  and
x = np.array([[1],[2]])
print(x.shape)

print()
y = np.array8[[1,2,3],[1,2,3]]
print(y.shape)

print()
print(x+y)






