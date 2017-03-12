###################################################
#Lempel Ziv code
###################################################

def maxmatch(T,p,w=2**12-1,max_length=2**5-1):
   """ finds a maximum match of length k<=2**5-1 in a
   w long window, T[p:p+k] with T[p-m:p-m+k].
   Returns m (offset) and k (match length) """
   assert isinstance(T,str)
   n=len(T)
   maxmatch=0
   offset=0
   for m in range(1,min(p+1,w)):
      k = 0
      while k<min(max_length,n-p)and T[p-m+k] == T[p+k]:
        # at this point, T[p-m:p-m+k]==T[p:p+k]
        k = k+1
      if maxmatch<k:  
         maxmatch=k
         offset=m
   return offset,maxmatch
# returned offset is smallest one (closest to p) among
# all max matches (m starts at 1)


def lz77_compress2(text,w=2**12-1,max_length=2**5-1):
   """LZ77 compression of an ascii text. Produces
      a list comprising of either ascii character
      or by a pair [m,k] where m is an offset and
      k is a match (both are non negative integers)"""
   result = []
   out_string=""
   n=len(text)
   p=0
   while p<n:
      if ord(text[p])>=128: continue
      m,k=maxmatch(text,p,w,max_length)
      if k<3:   # modified from k<2
         result.append(text[p]) #  a single char
         p+=1
      else:
         result.append([m,k])   # three or more chars in match
         p+=k
   return(result)  # produces a list composed of chars and pairs
            

def inter_to_bin(lst,w=2**12-1,max_length=2**5-1):
   """ converts intermediate format compressed list
       to a string of bits"""
   offset_width=math.ceil(math.log(w,2))
   match_width=math.ceil(math.log(max_length,2))
#   print(offset_width,match_width)   # for debugging
   result=[]
   for elem in lst:
      if type(elem)==str:
         result.append("0")
         result.append('{:07b}'.format(ord(elem)))
      elif type(elem)==list:
         result.append("1")
         m,k=elem
         result.append('{num:0{width}b}'.format
                       (num=m, width=offset_width))
         result.append('{num:0{width}b}'.
                       format(num=k, width=match_width))
         
   return "".join(ch for ch in result)
   

###################################################
#Extensions
###################################################


def lz77_compress2_no_future(text,w=2**12-1,max_length=2**5-1):
    """ Variation of lz77_compress2 disabling 'looking into the future """
   result = []
   out_string=""
   n=len(text)
   p=0
   while p<n:
      if ord(text[p])>=128: continue
      m,k = maxmatch_new(text,p,w,max_length) #maxmatch_new is called here!
      if k<3:  
         result.append(text[p]) #  a single char
         p+=1
      else:
         result.append([m,k])   # three or more chars in match
         p+=k
   return(result)

def test_lz77_compress2_no_future():
    if lz77_compress2_no_future("aaaaaa") != ['a', 'a', 'a', [3,3]] :
        print("error in maxmatch_new()")
       
def maxmatch_new(T,p,w=2**12-1,max_length=2**5-1):
    """ Helper function for lz77_compress2_no_future """
   assert isinstance(T,str)
   n = len(T)
   maxmatch = 0
   offset = 0
   for m in range(1, min(p+1, w)):
      k = 0
      while k < min(n-p, max_length, m) and T[p-m+k] == T[p+k]:
        k += 1
        # at this point, T[p-m:p-m+k]==T[p:p+k]
      if maxmatch < k:  
         maxmatch = k
         offset = m
   return offset, maxmatch
