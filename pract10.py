                           #divide and conquer    PRACTICAL :10
import numpy as np
def split(matrix):
             row,col = matrix.shape
             row2,col2 = row//2,col//2
             return matrix[row2:, col2:], matrix[row2: ,col2:], matrix[row2: ,col2:]

def strassen(x,y):
             #Base case when size of matrices is 1*1
             if len(x):
                          return x*y
             #Splitting the matrices into qutrants .this will done recursively
             #unit the base case is reached.
             a,b,c,d = split(x)
             e,f,g,h = split(y)
             #Computing the 7Product ,recursively(p1,p2,p3.....p7)
             p1=strassent(a,f-h)
             p2=strassent(a+b,h)
             p3=strassent(c+d,e)
             p4=strassent(d,g-e)
             p5=strassent(a+d,e+h)
             p6=strassent(b-d,g+h)
             p7=strassent(a-c,e+f)
             #computing the value of the 4 quadrants of the final matrix c
             c11 = p5+p4-p2+p6
             c12 = p1+p2
             c21 = p3+p4
             c22 = p1+p5-p3-p7
             c =np.vstack((np.hstack((c11,c12)),np.hstack((c21,c22))))
             return c
