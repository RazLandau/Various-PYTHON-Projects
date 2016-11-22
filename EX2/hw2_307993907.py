#Skeleton file for HW2 - Winter 2016-2017 - extended intro to CS

#Add your implementation to this file

#You may add other utility functions to this file,
#but you may NOT change the signature of the existing ones.

#Change the name of the file to hw2_<your ID number> (extension .py).

import time

############
# QUESTION 1
############

# 1c
def reverse_sublist(lst,start,end):
    for i in range((end - start) // 2):
        lst[start + i], lst[end - 1 - i] = lst[end - 1 - i], lst[start + i]

# 1d
def divide_list(lst):
    pivot = lst[0]
    smaller = [i for i in lst if i<pivot]
    greater = [i for i in lst if i>pivot]
    return smaller + [pivot] + greater

# 1e
def divide_list_inplace(lst):
    if len(lst) < 2:
        return
    pivot = lst[0]
    pivot_index = 0
    for i in range(1, len(lst)):
        if lst[i] < pivot:
            lst[pivot_index + 1], lst[i] = lst[i], lst[pivot_index + 1]
            lst[pivot_index], lst[pivot_index + 1] = lst[pivot_index + 1], lst[pivot_index]
            pivot_index += 1
    
############
# QUESTION 2b
############

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

############
# QUESTION 3b
############

def inc(binary):
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
    
        

############
# QUESTION 4b
############

# 4a
def sum_divisors(n):
    max_div = int(n**0.5)
    div_sum = 0
    for i in range(1, max_div+1):
        if n % i == 0 and i != n:
            div_sum += i
            sec_div = n // i
            if sec_div < n and sec_div != i:
                div_sum += sec_div
    return div_sum

# 4b
def is_perfect(n):
    pass #replace this with your code

# 4c
def count_perfect_numbers(limit):
    pass #replace this with your code

#4d
def is_finite(n):
    prev_sums = []
    div_sum = n
    while div_sum > 0:
        prev_sums.append(div_sum)
        div_sum = sum_divisors(div_sum)
        if div_sum in prev_sums:
            return False
    return True


#4e
def cnt_finite(limit):
    sum = 0
    for i in range (1, limit+1):
        if is_finite(i):
            sum+=1
    return sum


############
# QUESTION 5
############

# 5a
def has_common(s1,s2,k):
    if len(s1)<k or len(s2)<k:
       return False
    something = []
    for i in range (0, len(s1)-k+1):
        something.append(s1[i:i+k])
    for i in something:
        if i in s2:	
            return True
    return False

def lcs_length_1(s1, s2):
    k=1
    while has_common(s1,s2,k) == True:
        k+=1
    return k-1

#5b
def lcs_length_2(s1, s2):
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

#5c
import random
def gen_str(n, alphabet):
    return "".join([random.choice(alphabet) for i in range(n)])

###Amir's code:
##n=4000
##alphabet = "abcdefghijklmnopqrstuvwxyz"
##print("two random strings of length", n)
##s1 = gen_str(n, alphabet)
##s2 = gen_str(n, alphabet)
##
##t0 = time.clock()
##res1 = lcs_length_1(s1,s2)
##t1 = time.clock()
##print("lcs_length_1", res1, t1-t0)
##
##t0 = time.clock()
##res2 = lcs_length_2(s1,s2)
##t1 = time.clock()
##print("lcs_length_2", res2, t1-t0)

###Michal's code
##n=4000
##alphabet = "abcdefghijklmnopqrstuvwxyz"
##print("two identical random strings of length", n)
##s1 = gen_str(n, alphabet)
##s2 = s1
##
##t0 = time.clock()
##res1 = lcs_length_1(s1,s2)
##t1 = time.clock()
##print("lcs_length_1", res1, t1-t0)
##
##t0 = time.clock()
##res2 = lcs_length_2(s1,s2)
##t1 = time.clock()
##print("lcs_length_2", res2, t1-t0)

########
# Tester
########

def test():
    
    lst = [1,2,3,4,5]
    reverse_sublist (lst,0,4)
    if lst != [4, 3, 2, 1, 5]:
        print("error in reverse_sublist()")        
    lst = ["a","b"]
    reverse_sublist (lst,0,1)
    if lst != ["a","b"]:
        print("error in reverse_sublist()")
    lst = [1,2,3,4,5]
    reverse_sublist (lst,0,4)
    if lst != [4, 3, 2, 1, 5]:
        print("error in reverse_sublist()")  

    lst = [1,2,3,4,5]
    lst_div = divide_list(lst)
    if lst_div == None:
        print("error in divide_list()")
    if lst_div != None and len(lst_div) != 5:
        print("error in divide_list()")
    if lst_div != None and lst_div[0] != 1:
        print("error in divide_list()")
    lst = [3,2,1,4,5]
    lst_div = divide_list(lst)
    if lst_div == None:
        print("error in divide_list()")

    
    if lst_div != None and \
       (lst_div[0] >= 3 or \
       lst_div[1] >= 3 or \
       lst_div[2] != 3 or \
       lst_div[3] <= 3 or \
       lst_div[4] <= 3):
        print("error in divide_list()")
    #verify that the original list did not change
    if lst[0] != 3 or \
       lst[1] != 2 or \
       lst[2] != 1 or \
       lst[3] != 4 or \
       lst[4] != 5:
        print("error in divide_list()")
    

    lst = [1,2,3,4,5]
    divide_list_inplace(lst)
    if lst[0] != 1:
        print("error in divide_list_inplace()")
    lst = [3,2,1,4,5]
    divide_list_inplace(lst)
    if lst[0] >= 3 or \
       lst[1] >= 3 or \
       lst[2] != 3 or \
       lst[3] <= 3 or \
       lst[4] <= 3:
        print("error in divide_list_inplace()")

    if power_new(2,3) != 8:
        print("error in power_new()")

    if inc("0") != "1" or \
       inc("1") != "10" or \
       inc("101") != "110" or \
       inc("111") != "1000" or \
       inc(inc("111")) != "1001":
        print("error in inc()")
 
    if sum_divisors(6)!=6 or \
       sum_divisors(4)!=3:        
        print("error in sum_divisors()")

    if is_finite(6) or  \
       not is_finite(4) :
        print("error in is_finite()")

    if cnt_finite(6) != 5:
        print("error in cnt_finite()")
       
    if has_common("ababc", "dbabca", 5) != False or \
       has_common("ababc", "dbabca", 4) != True or \
       has_common("ababc", "dbabca", 3) != True or \
       has_common("", "dbabca", 2) != False or \
       lcs_length_1("ababc", "dbabca") != 4:
        print("error in has_common()")
   
    if lcs_length_2("ababc", "dbabca") != 4 or \
       lcs_length_2("dbabca", "ababc") != 4 or \
       lcs_length_2("xxx", "ababc") != 0 :
        print("error in lcs_length_2()")



