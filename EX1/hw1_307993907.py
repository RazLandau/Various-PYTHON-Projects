
#Question 3
in_file = "our_input.txt"
out_file = "output.txt"
f=open(out_file, 'w')
for line in open(in_file, 'r'):
    f.write(str(len(str.split(line)))+'\n')
f.close()

#**************************************************************

#Question 5
k = 9
n = 100
for x in range (1, n+1):
    if x%k==0 and str(k) in str(x):
        print("boom-boom!")
    elif x%k==0 or str(k) in str(x):
        print("boom!")
    else:
        print(x)

#**************************************************************

#Question 6
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
