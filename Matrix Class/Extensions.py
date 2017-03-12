from matrix import *

def upside_down(im):
    ''' Turn image upside-down '''
    n,m = im.dim()
    result = Matrix(n,m)
    for i in range(n):
        for j in range(m):
            result[n-1-i,j] = im[i,j]
    return result

def items(mat):
    ''' Flatten mat elements into a list '''
    n,m = mat.dim()
    lst = [mat[i,j] for i in range(n) for j in range(m)]
    return lst

def local_operator(A, op, k=1):
    ''' Invokes given operator on k-size squares in mat '''
    n,m = A.dim()
    res = A.copy()  # brand new copy of A
    for i in range(k,n-k):
        for j in range(k,m-k):
            res[i,j] = op(items(A[i-k:i+k+1,j-k:j+k+1]))
    return res

def segment(im, thrd):
    ''' Binary segmentation of image im by threshold thrd '''
    n,m = im.dim()
    result = Matrix(n,m)
    for i in range(n) :
        for j in range(m) :
            result[i,j] = 0 if im[i,j] < thrd else 255
    return result

def dilate(im, k=1):
    ''' Dilates image '''
    return local_operator(im, lambda x : 0 if 255 not in x else 255, k)

def diff(A, B):
    ''' operator "-" '''
    assert A.dim()==B.dim()
    n,m = B.dim()
    result = Matrix(n,m)
    for i in range(n) :
        for j in range(m) :
            result[i,j] = A[i,j]-B[i,j]
    return result

def edges(im, k, thr):
    ''' Return image of all boarders in given image '''
    return diff(dilate(segment(im,thr), k), segment(im,thr))

def test():
    m1 = Matrix(4,4,0)
    m1[0,0] = 20
    m1[1,0] = 60
    m2 = segment(m1,10)
    if m2.rows != [[255, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]:
        print("error in segment()")
    m3 = dilate(m2,1)
    if m3.rows != [[255, 0, 0, 0], [255, 255, 0, 0], [0, 255, 0, 0], [0, 0, 0, 0]]:
        print("error in dilate()")
    m4 = diff(m3,m2)
    if m4.rows != [[0, 0, 0, 0], [0, 255, 0, 0], [0, 255, 0, 0], [0, 0, 0, 0]]:
        print("error in diff()")
    if edges(m1,1,10) != m4:
        print("error in edges()")
