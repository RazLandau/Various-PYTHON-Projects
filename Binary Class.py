class Binary():
    def __init__(self, s):
        """ represent a binary number as a string """
        assert type(s)==str
        assert s.count("0") + s.count("1") == len(s)
        self.s = s

    def __repr__(self):
        return "0b" + self.s

    def length(self):
        return len(self.s)

    def __eq__(self, other):
        return self.s == other.s

    def __lt__(self, other):
        if self.length() < other.length():
            return True
        if self.length() > other.length():
            return False
        if self == other:
            return False
        for i in range(self.length()):
            if self.s[i] < other.s[i]:
                return True
            if self.s[i] > other.s[i]:
                return False
        return False

    def __add__(self, other):
        """ operator + """
        def helper_add(a,b):
            if not a or not b:
                return a or b           
            index = -1
            carry = 0
            result = []
            while -index <= max(len(a), len(b)):
                x = int(a[index]) if -index <= len(a) else 0
                y = int(b[index]) if -index <= len(b) else 0
                carry, remainder = divmod(x + y + carry, 2)
                result.append(remainder)
                index -= 1        
            if carry:
                result.append(carry)
            return ''.join(map(str, reversed(result)))
        return Binary(helper_add(self.s, other.s))
        
    def is_power_of_two(self):
        """ True if self is a power of 2, else - False """
        if self.s == '0':
            return False
        return self.s[1:]=='0'*(self.length()-1)

    def largest_power_of_two(self):
        """ return the largest power of 2 which is <= self """
        return 2**(self.length()-1)

    def div3(self):
        """ Returns remainder of self divided by 3 """
        cnt = Binary("0")
        while cnt < self:
            cnt = cnt + Binary("11")
        div = 0
        if self+Binary("1") == cnt: #remove True add your condition here
            div = 2
        if self+Binary("10") == cnt: #remove True add your condition here
            div = 1
        return div

    def div3_new(self):
        """ Returns remainder of self divided by 3 """
        div = 0
        d = {(0,'0'):0, (0,'1'):1, (1,'0'):2, \
             (1,'1'):0, (2,'0'):1, (2,'1'):2}
        for i in self.s:
            div = d[(div,i)]
        return div
