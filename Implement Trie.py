from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
class Node:
    def __init__(self):
        self.NodeLinks = [0]*26
        self.Flag = False

Root = Node()
RtCopy = Root

class Trie :
    def __init__(self) :
        self.Root = Root
        self.RtCopy = Root
    
    def insert(self, Word) :
        self.Root = Root
        self.RtCopy = Root
        for letter in Word:
            if(self.Root.NodeLinks[ord(letter)-97] == 0):
                self.NextLink = Node()
                self.Root.NodeLinks[ord(letter)-97] = self.NextLink
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                self.Root = self.Root.NodeLinks[ord(letter)-97]
        self.Root.Flag = True

    
    def search(self, Word) :
        self.Root = Root
        for letter in Word:
            if(self.Root.NodeLinks[ord(letter)-97] != 0):
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                return False
        return self.Root.Flag == True

    def startWith(self, Word) :
        self.Root = Root
        SWith = True
        for letter in Word:
            if(self.Root.NodeLinks[ord(letter)-97] != 0):
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                SWith = False
                break
        return SWith

