class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # ++--++
        # loop over string and find "++"
        # cancatinate to a new list with the following 
        # 1. string before the current ++ index
        # 2. replace ++ to --
        # 3. rest of string

        new_list = []
        for i in range(len(s)): 
            if s[i:i+2] == "++":
                new_list.append(s[:i] + "--" + s[i+2:])
        return new_list

    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Use dictionary to determine
        # looping over string
        # if char is in dict, remove it
        # if char does not exist in dict, add it 
        # results:
        # if len of dict is 1, it is palindrome
        # if len of dict is 0, it is palindrome
        # if len of dict is above one, it is not a palindrome
        dict = {}
        for c in s:
            if c in dict:
                dict.pop(c)
            else:
                dict[c] = None
        return len(dict) <= 1

    def reverse_words(self, line):
        word_list = line.split()
        while word_list:
            word = word_list.pop()
            print word,

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


    # ["eqdf", "qcpr"]。
    #((‘q’ - 'e') + 26) % 26 = 12, ((‘d’ - 'q') + 26) % 26 = 13, ((‘f’ - 'd') + 26) % 26 = 2
    #((‘c’ - 'q') + 26) % 26 = 12, ((‘p’ - 'c') + 26) % 26 = 13, ((‘r’ - 'p') + 26) % 26 = 2
    def groupStrings(self, strings):  
        """ 
        :type strings: List[str] 
        :rtype: List[List[str]] 
        """  
        # create dict list for using tuple as key and string as value
        d = collections.defaultdict(list)  
        for s in strings:  
            shift = tuple([(ord(c) - ord(s[0])) % 26 for c in s])  
            d[shift].append(s)  
          
        return map(sorted, d.values())  

