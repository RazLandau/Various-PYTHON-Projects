from matrix import *

def fingerprint(mat):
    assert isinstance(mat,Matrix)
    k,makesure = mat.dim()
    assert k==makesure

    return sum(mat[i,j] for i in range(k) for j in range(k))

def move_right(mat, i, j, k, fp):
    """ Move k-size square in mat 1 step right """
    result = fp
    for l in range(k):
        result = result - mat[i+l,j] + mat[i+l,j+k]
    return result

def move_down(mat, i, j, k, fp):
    """ Move k-size square in mat 1 step down """
    result = fp
    for l in range(k):
        result = result - mat[i,j+l] + mat[i+k,j+l]
    return result
    
def has_repeating_subfigure(mat, k):
    """ Check if mat has repeating subfigure of size k
    using Karp-Rabin Algorithm """ 
    n,m=mat.dim()
    fps_lst = [[0]*(m-k+1) for i in range(n-k+1)]
    for i in range(n-k+1) :
        for j in range(m-k+1) :
            if i == 0 and j == 0:
                 fps_lst[i][j] = fingerprint(mat[0:k,0:k])
            elif  i != 0 and j == 0:  
                fps_lst[i][j] = move_down(mat,i-1,0,k,fps_lst[i-1][0])               
            elif j !=0:
                fps_lst[i][j] = move_right(mat,i,j-1,k,fps_lst[i][j-1])
    fps_set = set()
    for i in range(n-k+1) :
        for j in range(m-k+1) :
            fp = fps_lst[i][j]
            if fp in fps_set :
                return True
            else :
                fps_set.add(fp)
    return False

def problematic_matrix():
    """ Return mat so that has_repeating_subfigure(mat) = false-positive """
    im = Matrix(4,4)
    lst = [0,128,0,255]
    for i in range(4):
        for j in range(4):
            im[i,j] = lst[i]
    return im

def test():
    im = Matrix.load("./sample.bitmap")
    k = 2
    if fingerprint(im[:k,:k]) != 384 or \
       fingerprint(im[1:k+1,1:k+1]) != 256 or \
       fingerprint(im[0:k,1:k+1]) != 511:
        print("error in fingerprint()")
    if move_right(im, 0, 0, k, 384) != 511:
        print("error in move_right()")
    if move_down(im, 0, 1, k, 511) != 256:
        print("error in move_down()")
    
    if has_repeating_subfigure(im, k) != True or\
       has_repeating_subfigure(im, k=3) != False:
        print("error in repeating_subfigure()")

    if has_repeating_subfigure(problematic_matrix(),3) != True:
       print("error in problemetic_matrix")
