from random import *

class Polynomial():
    def __init__(self, coeffs_lst):
        self.coeffs = coeffs_lst
        
    def __repr__(self):
        terms = [" + ("+str(self.coeffs[k])+"*x^" + \
                 str(k)+")" \
                 for k in range(len(self.coeffs)) \
                 if self.coeffs[k]!=0]
        terms = "".join(terms)
        if terms == "":
            return "0"
        else:
            return terms[3:] #discard leftmost '+'

    def degree(self):
        """ Return Polynomial highest power """
        return len(self.coeffs)-1

    def evaluate(self, x):
        """ Returns Polynomial(x) """
        def helper_evaluate(self, x, i):
            if i >= len(self.coeffs):
                return 0
            return self.coeffs[i] + x*helper_evaluate(self, x, i+1)
        return helper_evaluate(self, x, 0)

    def derivative(self):
        """ Returns Polynomial' """
        return Polynomial([i*self.coeffs[i] \
                           for i in range(1,len(self.coeffs))])

    def __eq__(self, other):
        """ Operator '==' """
        assert isinstance(other, Polynomial)  
        if len(self.coeffs) != len(other.coeffs):
            return False
        for i in range(len(self.coeffs)):
            if self.coeffs[i] != other.coeffs[i]:
                return False
        return True

    def __add__(self, other):
        """ Operator '+' """
        assert isinstance(other, Polynomial)  
        max_poly,min_poly = (self,other) \
                            if self.degree() >= other.degree() \
                            else (other,self)
        return Polynomial([max_poly.coeffs[i]+min_poly.coeffs[i] \
                           if i<len(min_poly.coeffs) \
                           else max_poly.coeffs[i] \
                           for i in range(len(max_poly.coeffs))])
            
    def __neg__(self):
        """ Operator '-x' """
        return self * Polynomial([-1])
        #return Polynomial([-coeff for coeff in self.coeffs])

    def __sub__(self, other):
        """ Operator 'x-y' """
        assert isinstance(other, Polynomial)  
        return self + (-other)

    def __mul__(self, other):
        """ Operator '*' """
        assert isinstance(other, Polynomial)  
        return Polynomial([sum([self.coeffs[i]*other.coeffs[k-i] \
                                for i in range(max([0,k-len(other.coeffs)+1]),1+min([k,len(self.coeffs)-1]))]) \
                           for k in range(len(self.coeffs)+len(other.coeffs)-1)])

    def find_root(self):
        """ Return x so that Polynomial(x)=0 """
        f = lambda x: self.evaluate(x)
        return NR(f, diff_param(f))

## code for Newton Raphson, needed in find_root ##
from random import *

def diff_param(f,h=0.001):
    return (lambda x: (f(x+h)-f(x))/h)


def NR(func, deriv, epsilon=10**(-8), n=100, x0=None):
    if x0 is None:
        x0 = uniform(-100.,100.)
    x=x0; y=func(x)
    for i in range(n):
        if abs(y)<epsilon:
            #print (x,y,"convergence in",i, "iterations")
            return x
        elif abs(deriv(x))<epsilon:
            #print ("zero derivative, x0=",x0," i=",i, " xi=", x)
            return None
        else:
            #print(x,y)
            x = x- func(x)/deriv(x)
            y = func(x)
    #print("no convergence, x0=",x0," i=",i, " xi=", x)
    return None

def test():
    q = Polynomial([0, 0, 0, 6])
    if str(q) != "(6*x^3)":
        print("error in Polynomial.__init__ or Polynomial.in __repr__")
    if q.degree() != 3:
        print("error in Polynomial.degree")
    p = Polynomial([3, -4, 1])
    if p.evaluate(10) != 63:
        print("error in Polynomial.evaluate")
    dp = p.derivative()
    ddp = p.derivative().derivative()
    if ddp.evaluate(100) != 2:
        print("error in Polynomial.derivative")
    if not p == Polynomial([3, -4, 1]) or p==q:
        print("error in Polynomial.__eq__")
    r = p+q
    if r.evaluate(1) != 6:
        print("error in Polynomial.__add__")
    if not (q == Polynomial([0, 0, 0, 5]) + Polynomial([0, 0, 0, 1])):
        print("error in Polynomial.__add__ or Polynomial.__eq__")
    if (-p).evaluate(-10) != -143:
        print("error in Polynomial.__neg__")
    if (p-q).evaluate(-1) != 14:
        print("error in Polynomial.__sub__")
    if (p*q).evaluate(2) != -48:
        print("error in Polynomial.__mult__")
    if (Polynomial([0])*p).evaluate(200) != 0:
        print("error in Polynomial class")
    root = p.find_root()
    if root-3 > 10**-7 and root-1 > 10**-7:
        print("error in Polynomial.find_root")
