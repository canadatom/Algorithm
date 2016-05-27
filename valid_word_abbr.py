class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.ds = collections.defaultdict(set)
        for word in dictionary:
            abbr = word[0], len(word), word[-1]
            self.ds[abbr].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = word[0], len(word), word[-1]
        return abbr not in self.ds or self.ds[abbr] == set([word])

# Your ValidWordAbbr object will be instantiated and called as such:
vwa = ValidWordAbbr(dictionary)
vwa.isUnique("word")
vwa.isUnique("anotherWord")