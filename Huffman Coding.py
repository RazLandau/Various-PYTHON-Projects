######################################################################
#######  Huffman Code ###########################################
######################################################################

def purify(text):
  """ Discards non ascii characters from text"""
  return "".join(ch for ch in text
                 if ord(ch)<128)

def str_to_bin(text):
  """ translates text to binary reprersentation using
  7 bits per character. Non ascii characters are discarded"""
  return "".join(['{:07b}'.format(ord(ch)) for ch in text])

def char_count(text):
    """ counts the number of occurances of ascii characters -
    ord(ch)<128, in a text. Returns a dictionary, with keys 
    being the observed characters, values being the counts """
    d = {}
    for ch in text:
        if ord(ch)>=128: continue
        if ch in d:
            d[ch] = 1+d[ch]
        else:
            d[ch]=1
    return d

def build_huffman_tree(letter_count):
    """ recieves dictionary with char:count entries
        generates a LIST of letters representing
        the binary Huffman encoding tree"""
    queue = [(x, px) for x,px in letter_count.items()]
    while len(queue) > 1:
    # combine two smallest elements
        a, pa = extract_min(queue)   # smallest in queue
        b, pb = extract_min(queue)   # next smallest
        chars = [a,b]
        weight = pa+pb # combined weight
        queue.append((chars,weight)) # insert new node
        # print(queue)   # to see what whole queue is
        # print()
    x, px = extract_min(queue) # only root node left 
    return x  # total weight

def extract_min(queue):
    P = [px for x,px in queue]
    return queue.pop(P.index(min(P)))

def generate_code(huff_tree, prefix=""):
    """ receives a Huffman tree with embedded encoding,
        and a prefix of encodings.
        returns a dictionary where characters are
        keys and associated binary strings are values."""
    if isinstance(huff_tree, str): # a leaf
        return {huff_tree: prefix}
    else:
        lchild, rchild = huff_tree[0], huff_tree[1]
        codebook = {}

        codebook.update( generate_code(lchild, prefix+'0'))
        codebook.update( generate_code(rchild, prefix+'1'))
        #   oh, the beauty of recursion...
        return codebook
    
def compress(text, encoding_dict):
  """ compress text using encoding dictionary """
  assert isinstance(text, str)
  return "".join(encoding_dict[ch] for ch in text if ord(ch)<=128)


def build_decoding_dict(encoding_dict):
   """build the "reverse" of encoding dictionary"""
   return {y:x for (x,y) in encoding_dict.items()}
  # return {y:x for x,y in encoding_dict.items()} # OK too
  
def decompress(bits, decoding_dict):
   prefix = ""
   result = []
   for bit in bits:
      prefix += bit
      if prefix in decoding_dict:
          result.append(decoding_dict[prefix])
          prefix = ""
   assert prefix == "" # must finish last codeword
   return "".join(result)  # converts list of chars to a string

######################################################################
#######  Extensions #######################################
######################################################################

asci = str.join("",[chr(c) for c in range(128)])

def compression_ratio(text, corpus):
  """ Checks Huffman's compression ratio """
  d = generate_code(build_huffman_tree(char_count(corpus)))
  len_compress = len(compress(text, d))
  len_unicode = len(text)*7
  return len_compress/len_unicode

def weighted_length(D, W):
  """ Return weighted length for given weights of given decodes """
  return sum([W[i]*len(D[i]) for i in range(len(D))])                               

def optimal(D, W):
  """ Checks if given decode is optimal """
  string = ""
  for i in range(len(D)):
      string = string + chr(ord('a')+i)*W[i]
  return weighted_length(D, W) == \
      len(compress(string, generate_code(build_huffman_tree(char_count(string)))))

def test():
    if weighted_length(["0", "11", "10"], [5, 1, 3]) != 13:
        print("error in weighted_length()")
    if optimal(["0", "11", "10"], [5, 1, 3]) != True:
        print("error in optimal()")
    if optimal(["0", "11", "10"], [3, 1, 5]) != False:
        print("error in optimal()")










