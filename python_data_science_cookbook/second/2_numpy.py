import numpy as np

a_list = [1,2,3]
an_array = np.array(a_list)
print(an_array)
an_array = np.array(a_list, dtype=float)
print(an_array)
a_listoflist = [[1,2,3],[5,6,7],[8,9,10]]
a_matrix = np.matrix(a_listoflist,dtype=float)

def display_shape(a):
    print("")
    print(a)
    print("")
    print("Number of elements in a = %d"%a.size)
    print("Number of dimensions in a = %d"%a.ndim)
    print("Rows and Columns in a ", a.shape)
    print("")

display_shape(a_matrix)

create_array = np.arange(1, 10,dtype=float)
display_shape(create_array)

create_array = np.linspace(1, 10)
display_shape(create_array)

create_array = np.logspace(1, 10, base= 10.0)
display_shape(create_array)

create_array = np.arange(1,10,2,dtype=int)
display_shape(create_array)

ones_matrix = np.ones((3,3))
display_shape(ones_matrix)

zeros_matrix = np.zeros((3,3))
display_shape(zeros_matrix)

identity_matrix = np.eye(N=3, M=3, k=0)
display_shape(identity_matrix)
identity_matrix = np.eye(N=3, k=1)
display_shape(identity_matrix)

a_matrix = np.arange(9).reshape(3,3)
display_shape(a_matrix)

back_to_array = a_matrix.reshape(-1)
display_shape(back_to_array)

a_matrix = np.arange(9).reshape(3,3)
back_to_array = np.ravel(a_matrix)
display_shape(back_to_array)

a_matrix = np.arange(9).reshape(3,3)
back_array = a_matrix.flatten()
display_shape(back_array)



a_matrix = np.arange(9).reshape(3,3)
b_matrix = np.arange(9).reshape(3,3)

c_matrix = a_matrix + b_matrix
print("c_matrix = \n", c_matrix)

d_matrix = a_matrix*b_matrix
print("d_matrix = \n",d_matrix)

e_matrix = np.dot(a_matrix, b_matrix)
print("e_matrix = \n", e_matrix)
f_matrix = e_matrix.T


print("f_matrix = \n", f_matrix)
print("f_matrix, minimum = %d"%(f_matrix.min()))
print("f_matrix, maximum = %d"%(f_matrix.max()))
print("f_matrix, col sum", f_matrix.sum(axis=0))
print("f_matrix, row sum", f_matrix.sum(axis=1))




