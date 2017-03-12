
def words_per_line(in_file):
    ''' print number of word in each line in given file to new file '''
    out_file = "output.txt"
    f=open(out_file, 'w')
    for line in open(in_file, 'r'):
        f.write(str(len(str.split(line)))+'\n')
    f.close()

#**************************************************************


def k_boom(n, k):
    ''' simulation for parameterized "7-boom!" game '''
    for x in range (1, n+1):
        if x%k==0 and str(k) in str(x):
            print("boom-boom!")
        elif x%k==0 or str(k) in str(x):
            print("boom!")
        else:
            print(x)

#**************************************************************


def max_odds_sequence():
    ''' prints max sequence of odd numbers in given int '''
    num = int(input("Please enter a positive integer: "))
    num = str(num)
    length = 0
    start = -1
    seq = None
    cur_length = 0
    cur_seq = ""
    for digit in num:
        if int(digit)%2 == 0:
            cur_length = 0
            cur_seq = ""
        else:
            cur_length = cur_length + 1
            cur_seq = cur_seq + digit
            if cur_length > length:
                length = cur_length
                seq = cur_seq

    if seq != None:
        start = num.find(seq)

    print("The maximal length is", length)
    print("Sequence starts at", start)
    print("Sequence is", seq)

#**************************************************************

def reverse_sublist(lst,start,end):
    ''' reverse list from start index to end index inplace '''
    for i in range((end - start) // 2):
        lst[start + i], lst[end - 1 - i] = lst[end - 1 - i], lst[start + i]
        
#**************************************************************

def divide_list(lst):
    ''' returns new list divided by the 1st element '''
    pivot = lst[0]
    smaller = [i for i in lst if i<pivot]
    greater = [i for i in lst if i>pivot]
    return smaller + [pivot] + greater

#**************************************************************

def divide_list_inplace(lst):
    ''' returns a new list divided by the 1st elements inplace '''
    if len(lst) < 2:
        return
    pivot = lst[0]
    pivot_index = 0
    for i in range(1, len(lst)):
        if lst[i] < pivot:
            lst[pivot_index + 1], lst[i] = lst[i], lst[pivot_index + 1]
            lst[pivot_index], lst[pivot_index + 1] = lst[pivot_index + 1], lst[pivot_index]
            pivot_index += 1
            
#**************************************************************

def power_new(a,b):
    """ computes a**b using iterated squaring """
    result = 1
    b_bin = bin(b)[2:]
    reverse_b_bin = b_bin[: :-1]
    for bit in reverse_b_bin: 
        if bit == '1':
            result=result*a
        a=a*a
    return result

#**************************************************************

def inc(binary):
    ''' adds 1 to a binary number '''
    output = ""
    all_ones = True
    for i in range(len(binary) - 1, -1, -1):
        if binary[i] == '1':
            output = '0' + output
        else:
            all_ones = False
            output = '1' + output
            output = binary[0 : i] + output
            break
    if all_ones:
        output = '1' + output
    return output

#**************************************************************

def sum_divisors(n):
    ''' returns the sum of givien int divisors '''
    max_div = int(n**0.5)
    div_sum = 0
    for i in range(1, max_div+1):
        if n % i == 0 and i != n:
            div_sum += i
            sec_div = n // i
            if sec_div < n and sec_div != i:
                div_sum += sec_div
    return div_sum

#**************************************************************

def is_finite(n):
    ''' return true if given int's divisors list if finite, false otherwise '''
    prev_sums = []
    div_sum = n
    while div_sum > 0:
        prev_sums.append(div_sum)
        div_sum = sum_divisors(div_sum)
        if div_sum in prev_sums:
            return False
    return True

#**************************************************************

def cnt_finite(limit):
    ''' return number of int from 1 to limit (inclusive) which are a start
    of a finite divisors list '''
    sum = 0
    for i in range (1, limit+1):
        if is_finite(i):
            sum+=1
    return sum

#**************************************************************

def lcs_length_1(s1, s2):
    ''' returns the max length of mutual substrings in s1 and s2 '''
    k=1
    while has_common(s1,s2,k) == True:
        k+=1
    return k-1

def has_common(s1,s2,k):
    ''' return true if s1 and s2 has a mutual substring of length k '''
    if len(s1)<k or len(s2)<k:
       return False
    something = []
    for i in range (0, len(s1)-k+1):
        something.append(s1[i:i+k])
    for i in something:
        if i in s2:	
            return True
    return False

def lcs_length_2(s1, s2):
    ''' returns the max length of mutual substrings in s1 and s2 '''
    if len(s1) == 0 or len(s2) == 0:
        return 0
    m = [[0]*len(s2) for i in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] != s2[j]:
                m[i][j] = 0
            elif i == 0 or j == 0:
                m[i][j] = 1
            else:
                m[i][j] = m[i-1][j-1] + 1
    return max([max(l) for l in m])

#**************************************************************

def find_first_positive1(f):
    ''' returns first natural number so that f(n)>0 in O(n) '''
    n = 1
    while (f(n) <= 0):
        n += 1
    return n

def test_find_first_positive1():
    ''' Tester for find_first_positive1 '''
    f1, f2 = lambda x : x - 8, lambda y : y - 5
    res1, res2 = find_first_positive1(f1), find_first_positive1(f2)
    if res1 == None or res2 == None or res1 != 9  or \
       res2 != 6:
        print("error in find_first_positive1")

def find_first_positive2(f):
    ''' returns first natural number so that f(n)>0 in O(log(n)) '''
    limit = 2
    while f(limit)<=0:
        limit *= 2
    return find_first_positive_range(f,limit//2,limit-1)

def test_find_first_positive2():
    ''' Tester for find_first_positive2 '''
    res1, res2 = find_first_positive2(f1), find_first_positive2(f2)
    if res1 == None or res2 == None or res1 != 9  or \
       res2 != 6:
        print("error in find_first_positive2")


def find_first_positive_range(f, a, b):
    ''' returns first natural number so that a<=n<=b and f(n)>0 in O(log(n)) '''
    while b >= a:
        mid = a + ((b-a)//2)
        if f(mid) > 0 and (f(mid-1) <= 0 or mid  == a):
            return mid
        if f(mid) <=0:
            a = mid+1
        else:
            b = mid-1
    return None

def test_find_first_positive_range():
    ''' Tester for find_first_positive_range '''
    res1, res2 = find_first_positive_range(f1, 1, 9), \
                 find_first_positive_range(f1, 1, 3)
    if res1 == None or res1 != 9 or res2 != None:
        print("error in find_first_positive_range")

#**************************************************************

def sort_bitonic_list(blst):
    ''' Sorts bitonic list '''
    blst_max = find_bitonic_maximum(blst)
    return merge(blst[0:blst_max+1], blst[:blst_max:-1])

def test_test_sort_bitonic_list():
    ''' Tester for test_test_sort_bitonic_list '''
    if sort_bitonic_list([-3, 1, 2, 3, 80, 100, 6]) != [-3, 1, 2, 3, 6, 80, 100] :
        print("error in sort_bitonic_list")

def find_bitonic_maximum(blst):
    ''' Return index of max element in bitonic list '''
    length = len(blst)
    assert length > 0
    if length == 1:
        return 0
    if blst[0] > blst[1]:
        return 0
    if blst[length-1] > blst[length-2]:
        return length-1
    high = length-1
    low = 0
    while low < high:
        mid  = (low + high) // 2
        if blst[mid] > blst[mid-1] and blst[mid] > blst[mid+1]:
            return mid
        if blst[mid+1] > blst[mid]:
            low = mid+1
        else:
            high = mid-1
    return mid

def test_find_bitonic_maximum():
    if find_bitonic_maximum([-3, 1, 2, 3, 80, 100, 6]) != 5 :
        print("error in find_bitonic_maximum")

def merge(A, B):
    ''' Merge list A of size n and list B of size m
        A and B must be sorted! '''
    n = len(A)
    m = len(B)
    C = [0 for i in range(n + m)]

    a=0; b=0; c=0
    while a<n and b<m: #more element in both A and B
        if A[a] < B[b]:
            C[c] = A[a]
            a+=1
        else:
            C[c] = B[b]
            b+=1
        c+=1

    if a==n: #A was completed
        while b<m:
            C[c] = B[b]
            b+=1
            c+=1
    else: #B was completed
        while a<n:
            C[c] = A[a]
            a+=1
            c+=1
    return C

#**************************************************************

def sort_pairs(lst):
    ''' Sorts list of tuples of ints from 0-100 in O(n)'''
    result = []
    for i in range (0,100):
        for j in range (0,100):
            for item in lst:
                if (item[0] == i and item[1] == j):
                    result.append(item)
    return result

def test_sort_pairs():
    if sort_pairs([(9, 7), (78, 24), (9, 74), (53, 81), (40, 43), (79, 82), (84, 46), (68, 53), (92, 95), (60, 38), (20, 62), (72, 57)]) \
       != [(9, 7), (9, 74), (20, 62), (40, 43), (53, 81), (60, 38), (68, 53), (72, 57), (78, 24), (79, 82), (84, 46), (92, 95)]:
        print("error in sort_pairs")    

#**************************************************************

def equal(f1, f2):
    ''' Returns x so that f1(x) = f2(x) '''
    g = lambda x: f1(x) - f2(x)
    return NR(g, diff_param(g))

def test_equal():
    f1, f2 = lambda x:4*x+1, lambda x:-x+6
    if equal(f1,f2) == None or abs(equal(f1, f2) - 1) > 10**-7:
        print("error in equal")

def source(f,y):
    ''' Returns x so that f(x) = y '''
    g = lambda x: f(x) - y
    return NR(g, diff_param(g))

def test_source():
    lin = lambda x: x+3
    if source(lin,5) == None or abs(source(lin,5) - 2.0000000003798846) > 10**-7:
        print("error in source")

def inverse(f):
    ''' Return f^(-1) '''
    return lambda x: source(f, x)

def test_inverse():
    lin = lambda x: x+3
    if inverse(lin) == None or abs(inverse(lin)(5) - 1.9999999998674198) > 10**-7:
        print("error in inverse")   

def diff_param(f,h=0.001):
    ''' Returns f' '''
    return (lambda x: (f(x+h)-f(x))/h)
 
from random import *
def NR(func, deriv, epsilon=10**(-8), n=100, x0=None):
    ''' Return x so that f(x) = 0 using Newton-Raphsin '''
    if x0 is None:
        x0 = uniform(-100.,100.)
    x=x0; y=func(x)
    for i in range(n):
        if abs(y)<epsilon:
            print (x,y,"convergence in",i, "iterations")
            return x
        elif abs(deriv(x))<epsilon:
            print ("zero derivative, x0=",x0," i=",i, " xi=", x)
            return None
        else:
            print(x,y)
            x = x- func(x)/deriv(x)
            y = func(x)
    print("no convergence, x0=",x0," i=",i, " xi=", x)
    return None

#**************************************************************

def max_list22(L):
    ''' Return max element in list in O(log(n)) inplace '''
    return max22(L, 0, len(L)-1)

def test_max_list22():
    ''' Tester for max_list22 '''
    if max_list22([1,20,3]) != 20:
        print("error in max22()")
    if max_list22([1,20,300,400]) != 400:
        print("error in max22()")

def max22(L, left, right):
    ''' Return max element in list from left index to right index
    in O(log(n)) inplace '''
    if left == right:
        return L[left]
    mid = (left + right) // 2
    max_left = max22(L, left, mid)
    max_right = max22(L, mid + 1, right)
    return max(max_left, max_right)

#**************************************************************

def profit(value, size):
    ''' Solves good old profit problem '''
    max_profit = 0
    if size == 0:
        return 0
    for i in range(size):
        curr_profit = value[i] + profit(value, size-(i+1))
        if (curr_profit > max_profit):
            max_profit = curr_profit
    return max_profit

def test_profit():
    ''' Tester for profit '''
    if profit([1, 5, 8, 9], 4) != 10:
        print("error in profit()")
    if profit([2, 3, 7, 8, 9], 5) != 11:
        print("error in profit()")

def profit2(value, size):
    ''' Solves good old profit problem using memoization '''
    d = {}
    return profit_mem(value, size, d)

def test_profit2():
    ''' Tester for profit2 '''
    if profit2([1, 5, 8, 9], 4) != 10:
        print("error in profit2()")
    if profit2([2, 3, 7, 8, 9], 5) != 11:
        print("error in profit2()")

def profit_mem(value, size, d):
    ''' Helper method for profit2 '''
    max_profit = 0
    if size <= 0:
        return 0
    if size in d:
        return d[size]   
    for i in range(size):
        curr_profit = value[i] + profit_mem(value, size-(i+1), d)
        if (curr_profit > max_profit):
            max_profit = curr_profit
            d[size] = curr_profit
    return max(d.values())

#**************************************************************

def comp(s1,s2):
    ''' Compares 2 strings recursively '''
    if len(s1)==0 and len(s2)==0:
        return True
    if len(s1)==0 or len(s2)==0:
        return False
    if s1[0] != s2[0]:
        return False
    return comp(s1[1:], s2[1:])

def test_comp():
    ''' Tester for comp '''
    if comp("ab", "ab")!=True:
        print("error in comp()")
    if comp("", "")!=True:
        print("error in comp()")
    if comp("a", "ab")!=False:
        print("error in comp()")

def comp_ext(s1,s2):
    ''' Compares 2 string recursively, with special chars '+' (joker)
    and '*' (unbound joker) '''
    if len(s1)==0 and len(s2) == 0:
        return True
    if len(s1)==0 or len(s2)==0:
        return False
    if s1[0]=="+":
        return comp_ext(s1[1:], s2[1:])
    if s1[0]=="*":
        return comp_ext(s1[:0:-1], s2[:len(s2)-len(s1):-1])
    if s1[0] != s2[0]:
        return False
    return comp_ext(s1[1:], s2[1:])

def test_comp_ext():
    ''' Tester for comp_ext '''    
    if comp_ext("ab", "ab")!=True:
        print("error1 in comp_ext()")
    if comp_ext("", "")!=True:
        print("error2 in comp_ext()")
    if comp_ext("a", "ab")!=False:
        print("error3 in comp_ext()")
    if comp_ext("+", "a")!=True:
        print("error4 in comp_ext()")
    if comp_ext("+", "")!=False:
        print("error5 in comp_ext()")
    if comp_ext("a+b", "axb")!=True:
        print("error6 in comp_ext()")
    if comp_ext("a+b", "axxb")!=False:
        print("error7 in comp_ext()")
    if comp_ext("a*xyz", "abcxyz")!=True:
        print("error8 in comp_ext()")
    if comp_ext("a*", "a")!=False:
        print("error9 in comp_ext()")

#**************************************************************

def choose_sets(lst, k):
    ''' Returns a list of all possible subsets of given list '''
    if k <= 0:
        return [[]]
    elif lst == []:    # k is non negative int
        return []
    else:
        result = [lst[:1] + set_i for set_i in choose_sets(lst[1:], k-1)]
        result += choose_sets(lst[1:], k)
        return result

def test_choose_sets():
    ''' Tester for choose_sets '''
    if choose_sets([1,2,3,4], 0) != [[]]:
        print("error in choose_sets()")
    tmp = choose_sets(['a','b','c','d','e'], 4)
    if tmp == None:
        print("error in choose_sets()")
    else:
        tmp = sorted([sorted(e) for e in tmp])
        if tmp != [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'e'], ['a', 'b', 'd', 'e'], ['a', 'c', 'd', 'e'], ['b', 'c', 'd', 'e']]:
            print("error in choose_sets()")
    
#**************************************************************

def suffix_prefix_overlap(lst, k):
    """ Return list of all (i,j) in lst so that i's suffix and j's prefix
    of length k match in O(k*n^2) """
    return [(suffix, prefix) \
            for suffix in range(len(lst)) \
            for prefix in range(len(lst)) \
            if suffix != prefix and lst[suffix][-k:] == lst[prefix][:k]]
    return result

def suffix_prefix_overlap_hash1(lst, k):
    """ Return list of all (i,j) in lst so that i's suffix and j's prefix
    of length k match in O(k*n) """
    d = Dict(len(lst))
    for i in range(len(lst)):
        d.insert(lst[i][-k:],i)
    return [(suffix, prefix) \
            for prefix in range(len(lst)) \
            for suffix in d.find(lst[prefix][:k]) \
            if suffix != prefix]
    return result

class Dict:
    """ Used in suffix_prefix_overlap_hash1 """
    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries """
        self.table = [ [] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def __repr__(self):
        L = [self.table[i] for i in range(len(self.table))]
        return "".join([str(i) + " " + str(L[i]) + "\n" for i in range(len(self.table))])
              
    def insert(self, key, value):
        """ insert key,value into table
            Allow repetitions of keys """
        i = self.hash_mod(key) #hash on key only
        item = [key, value]    #pack into one item
        self.table[i].append(item) 

    def find(self, key):
        """ returns ALL values of key as a list, empty list if none """
        return [entry[1] \
                for entry in self.table[self.hash_mod(key)] \
                if entry[0] == key]
    
def suffix_prefix_overlap_hash2(lst, k):
    """ Return list of all (i,j) in lst so that i's suffix and j's prefix
    of length k match using python's dict class """    
    d = {}
    for i in range(len(lst)):
        suffix = lst[i][-k:]
        if suffix not in d:
            d[suffix] = [i]
        else:
            d[suffix] = d[suffix].append([i])
    return [(suffix, prefix) \
            for prefix in range(len(lst)) \
            for suffix in d[lst[prefix][:k]] \
            if suffix != prefix]
    return result

def test_suffix_prefix_overlap():
    """ Tester for suffix_prefix_overlap """
    s0 = "a"*100
    s1 = "a"*60+"b"*40
    s2 = "a"*10+"b"*40+"c"*50
    lst = [s0,s1,s2]
    k=50
    if suffix_prefix_overlap(lst, k) != [(0, 1), (1, 2)]:
        print("error in suffix_prefix_overlap")
    d = Dict(3)
    d.insert(56, "a")
    d.insert(56, "b")
    if d.find(56) != ['a', 'b'] and d.find(56) != ['b', 'a']:
       print("error in find")
    if(d.find(34) != []):
       print("error in find")
    if suffix_prefix_overlap_hash1(lst, k) != [(0, 1), (1, 2)]:
        print("error in suffix_prefix_overlap_hash1")
    if suffix_prefix_overlap_hash2(lst, k) != [(0, 1), (1, 2)]:
        print("error in suffix_prefix_overlap_hash2")

#**************************************************************

def generate_pascal():
    """ Generator for Pascal Triangle's rows """
    row = next_row([])
    while True:
        yield row
        row = next_row(row)

def test_generate_pascal():
    """ Tester for generate_pascal """
    gp = generate_pascal()
    if gp == None:
        print("error in generate_pascal()")
    elif next(gp)!=[1] or next(gp)!=[1,1] or next(gp)!=[1,2,1]:
        print("error in generate_pascal()")

def next_row(lst):
    """ Return next row in Pascal Triangle """
    if len(lst) == 0:
        return [1]
    result = [1 if i == len(lst) or i == 0 \
              else lst[i-1]+lst[i] \
              for i in range(len(lst)+1)]
    return result

def generate_bernoulli():
    """ Generator for Bernoulli Triangle's rows """
    gp = generate_pascal()
    while True:
        row = next(gp)
        yield [sum(row[:i+1]) for i in range(0,len(row))]

def test_generate_bernoulli():
    """ Tester for generate_bernoulli """
    gb = generate_bernoulli()
    if gb == None:
        print("error in generate_bernoulli()")
    elif next(gb)!=[1] or next(gb)!=[1,2] or next(gb)!=[1,3,4]:
        print("error in generate_bernoulli()")

#**************************************************************



